from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random
# Create your views here.
def index(request):
    return HttpResponse('<h1>Random</h>' + str(random.random()))

def create(request):
    return HttpResponse('CReate')

def read(request, id):
    return HttpResponse('REad!!'+id)