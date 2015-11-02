'''
Created on Oct 31, 2015

@author: sprasa7
'''
import datetime
import random
import string
import uuid
from random import randrange, randint
from datetime import timedelta

from .models import DateRange
from .models import Applicant

WORKFLOW_STATES = ["applied", "quiz_started", "quiz_completed", "onboarding_requested", "onboarding_completed", "hired", "rejected"]
LOCATIONS = ["San Francisco", "Chicago", "Seattle", "Austin", "New York", "Madison", "Milwaukee"]

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


def get_random_name():
    return ''.join(random.choice(string.lowercase) for i in range(20))

def get_random_email():
    return get_random_name() + "@gmail.com"

def get_random_phone():
    n = 10
    return ''.join(["%s" % randint(0, 9) for num in range(0, n)])

def get_random_location():
    return random.choice(LOCATIONS)

def get_random_workflow_state():
    return random.choice(WORKFLOW_STATES)

def get_random_date():
    start_date, end_date = datetime.date(2010, 1, 1), datetime.date(2015, 10, 31)
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start_date + timedelta(seconds=random_second)

def bootstrap_db_with_data_for_funnel_report(num_random_entries_to_generate):
    name, email, phone, location, workflow_state, created_at, updated_at = None, None, None, None, None, None, None
    
    inserted_counter = 0
    for counter in range(num_random_entries_to_generate):
        name = get_random_name().upper()
        email = get_random_email()
        phone = get_random_phone()
        location = get_random_location()
        workflow_state = get_random_workflow_state()
        created_at = get_random_date()
        updated_at = created_at
        applicant = Applicant(name=name, email=email, phone=phone, location=location, workflow_state=workflow_state, created_at=created_at, updated_at=updated_at)
        
        # Check because even though the values generated are random, they might still collide with existing data.
        # Don't try to insert such cases.
        if not Applicant.objects.filter(email=email).exists() and not Applicant.objects.filter(phone=phone).exists():
            inserted_counter += 1
            applicant.save()
            print("Inserted applicant id : %s", applicant)
            
    return "Inserted " + str(inserted_counter) + " random shopper applicants into DB"
