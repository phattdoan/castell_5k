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

    age_under_18 = 'Under 18'
    age_18_24 = '18-24'
    age_25_30 = '25-30'
    age_31_35 = '31-35'
    age_36_40 = '36-40'
    age_41_45 = '41-45'
    age_46_50 = '46-50'
    age_51_55 = '51-55'
    age_56_60 = '56-60'
    age_51_55 = '51-55'
    age_61_65 = '61-65'
    age_66_plus = '66+'

    AGE_GROUP = [
        (age_under_18, 'Under 18'),
        (age_18_24, '18-24'),
        (age_25_30, '25-30'),
        (age_31_35, '31-35'),
        (age_36_40, '36-40'),
        (age_41_45, '41-45'),
        (age_46_50, '46-50'),
        (age_51_55, '51-55'),
        (age_56_60, '56-60'),
        (age_51_55, '51-55'),
        (age_66_plus, '66+')
        ]

    age_group = models.CharField(
        max_length=50,
        choices=AGE_GROUP,
        default=age_18_24,
    )
    
    minutes = models.SmallIntegerField()
    seconds = models.SmallIntegerField()
    miliseconds = models.SmallIntegerField(null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    
    run_photo = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.first_name + self.last_name