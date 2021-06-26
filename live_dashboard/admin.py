from django.contrib import admin
from .models import *

class ResultAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
    'age_group', 'gender', 'minutes', 'seconds', 'date_completed']


    search_fields = ('first_name','last_name','age_group','gender',)

# Register your models here.
admin.site.register(Result, ResultAdmin)