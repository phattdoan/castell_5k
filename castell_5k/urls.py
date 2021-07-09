"""castell_5k URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from live_dashboard import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('castell_5k', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('overall/',views.overall, name='overall'),
    path('male_under_25/',views.male_under_25, name='male_under_25'),
    path('male_26_35/',views.male_26_35, name='male_26_35'),
    path('male_36_49/',views.male_36_49, name='male_36_49'),
    path('male_50_above/',views.male_50_above, name='male_50_above'),
    path('female_under_25/',views.female_under_25, name='female_under_25'),
    path('female_26_35/',views.female_26_35, name='female_26_35'),
    path('female_36_49/',views.female_36_49, name='female_36_49'),
    path('female_50_above/',views.female_50_above, name='female_50_above'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
