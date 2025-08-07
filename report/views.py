from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def intro(request):
    return HttpResponse("Hi HI. You're now on the reports app.")