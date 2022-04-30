from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'}

]

def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django hahaha
    </body>
    </html>
    ''')

def create(request):
    return HttpResponse('CReate')

def read(request, id):
    return HttpResponse('REad!!'+id)