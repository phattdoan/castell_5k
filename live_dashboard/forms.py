from django.forms import ModelForm
from django import forms
from .models import Result
from datetime import datetime

class ResultForm(ModelForm):
    age_under_25 = 'Under 25'
    age_26_35 = '26-35'
    age_36_49 = '36-49'
    age_50_over = '50+'

    AGE_GROUP = [
        (age_under_25 , 'Under 25'),
        (age_26_35 , '26-35'),
        (age_36_49 , '36-49'),
        (age_50_over , '50+'),
        ]

    M = 'Male'
    F = 'Female'
    GENDER_TYPE = [
        (M, 'Male'),
        (F, 'Female')
        ]

    gender = forms.ChoiceField(choices = GENDER_TYPE,  required=True)
    age_group = forms.ChoiceField(choices = AGE_GROUP, required=True)

    date_completed = forms.DateField(widget = forms.SelectDateWidget, initial=datetime.now())

    run_photo = forms.ImageField(label='Share your run photo', required=False)

    class Meta:
        model = Result
        fields = ['first_name', 'last_name', 'gender', 'age_group',
        'minutes', 'seconds', 'date_completed'
        , 'run_photo'
        ]