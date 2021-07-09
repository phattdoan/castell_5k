from django.db import models
from datetime import datetime 

class Result(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    M = 'Male'
    F = 'Female'
    GENDER_TYPE = [
        (M, 'Male'),
        (F, 'Female')
        ]

    gender = models.CharField(
        max_length=50,
        choices=GENDER_TYPE,
        default=F,
    )

    age_under_25 = 'Under 25'
    age_26_35 = '26-35'
    age_36_49 = '36-49'
    age_50_over = '50+'
    
    AGE_GROUP = [
        (age_under_25, 'Under 25'),
        (age_26_35, '26-35'),
        (age_36_49, '36-49'),
        (age_50_over, '50+')
        ]

    age_group = models.CharField(
        max_length=50,
        choices=AGE_GROUP,
        default=age_26_35,
    )
    
    minutes = models.SmallIntegerField()
    seconds = models.SmallIntegerField()
    miliseconds = models.SmallIntegerField(null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    
    run_photo = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.first_name + self.last_name