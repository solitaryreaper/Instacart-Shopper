'''
Created on Oct 31, 2015

@author: sprasa7
'''
import datetime
import uuid
from .models import DateRange
from .models import Applicant

def does_email_already_exist(email):
    '''
        Checks if an email already exists in the shopper database
    '''
    return Applicant.objects.filter(email=email).exists()

def does_phone_already_exist(phone):
    '''
        Checks if a phone number already exists in the shopper database
    '''
    return Applicant.objects.filter(email=phone).exists()

def get_unique_reference_id():
    '''
        Returns a unique reference id for new shopper applicants
    '''
    rid = uuid.uuid4()[0:8].upper()
    return rid

def get_nearest_previous_monday(date):
    '''
        Returns the previous monday for the given reference date
    '''
    last_monday = (date - datetime.timedelta(days=date.weekday()))
    return last_monday                          
                               
def get_nearest_next_sunday(date):
    '''
        Returns the next sunday for the given reference date
    '''
    next_sunday = (date + datetime.timedelta(days=-date.weekday()-1, weeks=1))
    return next_sunday 

def get_date_ranges(start_date, end_date):
    nearest_prev_monday = get_nearest_previous_monday(start_date)
    nearest_next_sunday = get_nearest_next_sunday(end_date)
    
    date_ranges = []
    curr_date = nearest_prev_monday
    while curr_date <= nearest_next_sunday:
        curr_start_date = curr_date
        curr_end_date = curr_date + datetime.timedelta(days=6)
        date_ranges.append(DateRange(curr_start_date, curr_end_date))

        # Increment it to the next monday
        curr_date = curr_end_date + datetime.timedelta(days=1)
        
    return date_ranges