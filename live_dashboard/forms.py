from django.forms import ModelForm
from django import forms
from .models import Result
from datetime import datetime

class ResultForm(ModelForm):
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