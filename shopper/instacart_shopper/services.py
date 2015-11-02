from .models import Applicant
from .utils import *
from django.db.models import Count
import collections

def check_if_valid_applicant(applicant):
    '''
        Runs all validations on the applicant
    '''
    is_valid_applicant, validation_failures = True, []
    
    # Check if email already present
    if Applicant.objects.filter(email=applicant.email).exists():
        is_valid_applicant = False
        validation_failures.append("Email " + applicant.email + " already exists.")
    
    # Check if phone number already present
    if Applicant.objects.filter(phone=applicant.phone).exists():
        is_valid_applicant = False
        validation_failures.append("Phone " + applicant.phone + " already exists.")    
    
    return (is_valid_applicant, validation_failures)

def get_shoppers_workflow_states_bw_dates(start_date, end_date):
    return Applicant.objects.filter(created_at__range=(start_date, end_date)).values('workflow_state').annotate(dcount=Count('workflow_state'))

def get_funnel_report(start_date, end_date):
    '''
        Generates the funnel report between the given date intervals
    '''
    funnel_report = collections.OrderedDict()
    date_ranges = get_date_ranges(start_date, end_date)
    for date_range in date_ranges:
        range_start = date_range.start_date
        range_end = date_range.end_date
        range_key = str(date_range)
        range_workflow_states = {}
        
        workflow_states = get_shoppers_workflow_states_bw_dates(range_start, range_end)
        if workflow_states:
            for state in workflow_states:
                state_name = state["workflow_state"]
                state_value = state["dcount"]
                range_workflow_states[state_name] = state_value
                
            print("%s" % (workflow_states))
        
        funnel_report[range_key] = range_workflow_states
        
    return funnel_report



