from django.shortcuts import render, redirect
from .models import Result
from .forms import ResultForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def submit(request):
    if request.method == 'GET':
        return render(request, 'submit.html', {'form':ResultForm()})
    else:
        try:
            form = ResultForm(request.POST, request.FILES)
            form.save()
            return redirect('overall')
        except ValueError:
            return render(request, 'submit.html', {'form':ResultForm(), 'error':'Bad data passed in. Try again.'})

def overall(request):
    results = Result.objects.order_by('minutes','seconds')

    return render(request, 'overall.html',{'results':results})

def male_under_25(request):
    results = Result.objects.filter(age_group='Under 25', gender='Male').order_by('minutes','seconds')

    return render(request, 'male_under_25.html',{'results':results})

def male_26_35(request):
    results = Result.objects.filter(age_group='26-35', gender='Male').order_by('minutes','seconds')

    return render(request, 'male_26_35.html',{'results':results})

def male_36_49(request):
    results = Result.objects.filter(age_group='36-49', gender='Male').order_by('minutes','seconds')

    return render(request, 'male_36_49.html',{'results':results})

def male_50_above(request):
    results = Result.objects.filter(age_group='50+', gender='Male').order_by('minutes','seconds')

    return render(request, 'male_50_above.html',{'results':results})

def female_under_25(request):
    results = Result.objects.filter(age_group='Under 25', gender='Female').order_by('minutes','seconds')

    return render(request, 'female_under_25.html',{'results':results})

def female_26_35(request):
    results = Result.objects.filter(age_group='26-35', gender='Female').order_by('minutes','seconds')

    return render(request, 'female_26_35.html',{'results':results})

def female_36_49(request):
    results = Result.objects.filter(age_group='36-49', gender='Female').order_by('minutes','seconds')

    return render(request, 'female_36_49.html',{'results':results})

def female_50_above(request):
    results = Result.objects.filter(age_group='50+', gender='Female').order_by('minutes','seconds')

    return render(request, 'female_50_above.html',{'results':results})