from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
		return HttpResponse("<h1>Hello, world.</h1>")

def about_us(request):
		return HttpResponse("About us.")

def subscribe(request):
		return HttpResponse("subscribe")

# return render(request, 'hello.html', {'name': 'World'})