from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages

from .models import Applicant
from .services import *
from .utils import *
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError

import json

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def home(request):
    return render(request, "instacart_shopper/home.html")

def background_check(request):
    logger.info("Request : %s", request)
    return render(request, "instacart_shopper/background_check.html")

def application_confirmation(request):
    request.session['email'] = request.session['reg_email']
    
    logger.debug("Saving applicant ..")
    applicant = Applicant(name=request.session['reg_name'], email=request.session['reg_email'], phone=request.session['reg_phone'], location=request.session['reg_location'])
    applicant.save()
    context = RequestContext(request, {'applicant': applicant})
    
    try:
        del request.session['reg_name']
        del request.session['reg_email']
        del request.session['reg_phone']
        del request.session['reg_location']
    except Exception as e:
        logger.error("Failed to delete session variables. Reason : %s", str(e))
    
    return render(request, 'instacart_shopper/application_confirmation.html', context)

def edit_application(request):
    applicant = Applicant.objects.filter(email=request.session['email'])
    context = RequestContext(request, {'applicant': applicant[0]})
    logger.debug("Applicant : %s" % str(applicant))
    return render(request, 'instacart_shopper/edit_application.html', context)

def update_application(request):
    email = None
    if "email" in request.session:
        email = request.session['email']
        
    applicant = Applicant.objects.filter(email=email)[0]
    params = request.POST
        
    applicant.name = params['name']
    applicant.phone = params['phone']
    applicant.location = params['location']
    applicant.save()
    logger.info("Applicant : %s" % str(applicant))
    
    message = "Application details updated for " + email
    messages.info(request, message)      

    context = RequestContext(request, {'applicant': applicant})
    return render(request, 'instacart_shopper/login.html', context)
    
def login(request):
    email = None
    if "email" in request.POST:
        email = request.POST['email']
    # If login screen accessed in the current session using email, let it pass
    elif "email" in request.session:
        email = request.session['email']
    
    if not email:
        error_message = "Please login to access the application"
        messages.error(request, error_message)
        return render(request, 'instacart_shopper/home.html')
            
    if Applicant.objects.filter(email=email).exists():
        request.session['email'] = email
        applicant = Applicant.objects.filter(email=email)
        context = RequestContext(request, {'applicant': applicant[0]})
        logger.debug("Applicant : %s" % str(applicant))
        return render(request, 'instacart_shopper/login.html', context)
    else:
        error_message = "No applicant found with email " + email
        messages.error(request, error_message)
        return render(request, 'instacart_shopper/home.html')

def logout(request):
    try:
        del request.session['email']
    except Exception as e:
        logger.error("Failed to delete session variable. Reason : %s", str(e))
        
    return render(request, 'instacart_shopper/home.html')

def register(request):
    params = request.POST
    
    name = params['name']
    email = params['email']
    phone = params['phone']
    location = params['location']
    applicant = Applicant(name=name, email=email, phone=phone, location=location)
    logger.info("Applicant : %s" % str(applicant))
    
    request.session['reg_name'] = name
    request.session['reg_email'] = email
    request.session['reg_phone'] = phone
    request.session['reg_location'] = location
            
    applicant_validation = check_if_valid_applicant(applicant)
    is_valid_applicant = applicant_validation[0]
    validation_failures = applicant_validation[1]
    
    logger.info("Is Valid Applicant ? %s", is_valid_applicant)
    if is_valid_applicant:
        logger.debug("Redirecting to background check page.")
        return render(request, 'instacart_shopper/background_check.html')
    else:
        for failure in validation_failures:
            messages.add_message(request, messages.ERROR, failure)
            
        return render(request, 'instacart_shopper/home.html')
    
def funnel_analytics(request):
    '''
        Funnel Analysis for shoppers.
        
        Groups the workflow state of shoppers across various week buckets.
        Each bucket has counters for the various workflow states for that week.
    '''
    
    params = request.GET
    
    logger.debug("Parameters : %s" % (params))
    #Check if API called with right parameters
    if "start_date" not in params or "end_date" not in params or len(params) > 2:
        errorMessage = "API called with incorrect GET parameters " + str(params) + ". Please call with correct parameters : (start_date, end_date)"
        return HttpResponseBadRequest(errorMessage)
    
    start_date_str = request.GET['start_date']
    end_date_str = request.GET['end_date']
    
    #Check if API called with right values
    start_date, end_date = None, None
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except Exception as e:
        error_message = "API parameter values " + start_date_str + " or " + end_date_str + " is invalid. Please provide date value in YYYY-MM-DD format only."
        return HttpResponseBadRequest(error_message)
    
    if start_date > end_date:
        error_message = "Start date " + start_date_str + " can't be greater than End date " + end_date_str +". Please call API with correct parameters .."
        return HttpResponseBadRequest(error_message)
    
    #Catch any errors
    funnel_report = None
    try:
        logger.info("Generating funnel report bw (%s, %s)" % (start_date, end_date))
        funnel_report = get_funnel_report(start_date, end_date)
        logger.info("Generated funnel report : %s" % (funnel_report))
    except Exception as e:
        error_message = "API failed with internal server error : " + str(e)
        return HttpResponseServerError(error_message)
    
    return HttpResponse(json.dumps(funnel_report), content_type="application/json")

        
