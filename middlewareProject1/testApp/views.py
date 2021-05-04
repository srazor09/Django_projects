from django.shortcuts import render
from django.http import  HttpResponse
import logging
# Create your views here.

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)
logging.warning("Sourabh Logging Tutorials")


def welcome_view(request):
    print("This line printed by view function while processing request")
    #print(10/0)
    logger.error("Test!!")
    return HttpResponse('<h1> Custom middleware Demo </h1>')
