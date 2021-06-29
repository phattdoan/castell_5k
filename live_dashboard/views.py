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
            form = ResultForm(request.POST)
            newresult = form.save()
            return redirect('overall')
        except ValueError:
            return render(request, 'submit.html', {'form':ResultForm(), 'error':'Bad data passed in. Try again.'})

def overall(request):
    results = Result.objects.order_by('minutes','seconds')

    return render(request, 'overall.html',{'results':results})

def male_18_24(request):
    results = Result.objects.filter(age_group='18-24', gender='Male').order_by('minutes','seconds')

    return render(request, 'male_18_24.html',{'results':results})