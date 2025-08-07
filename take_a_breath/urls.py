"""
URL configuration for take_a_breath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from quote import views as quote_views
from report import views as report_views
from contact_us import views as contact_views

urlpatterns = [
    path('home/', quote_views.intro, name='quote_intro'),
    path('report/', report_views.intro, name='report_intro'),
    path('contact/', contact_views.intro, name='contact_intro'),
    path('admin/', admin.site.urls),
]
