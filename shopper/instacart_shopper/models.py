from django.db import models
from django.utils import timezone

class Applicant(models.Model):
    '''
        Models an instacart shopper
    '''
    
    id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(unique=True)
    location = models.CharField(max_length=100)
    workflow_state = models.CharField(max_length=100, default='applied')
    created_at = models.DateField(default=timezone.now())
    updated_at = models.DateField(default=timezone.now())
    
    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.id, self.name, self.email, self.phone, self.location, self.workflow_state, self.created_at, self.updated_at)
    
    
class DateRange(object):
    
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        
    def __str__(self):
        return "%s-%s" % (self.start_date, self.end_date)   
    
    
    
