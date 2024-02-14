from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(s):
	return HttpResponse("Hi welcome")

def dp(request):
	return HttpResponse("<h1>Welcome User</h2>")

def ry(request,z):
	return HttpResponse(f"Good Afternoon User {z}")

def hy(request,y,q):
	return HttpResponse(f"<h5>Name: <span style='color:red'>{y}</span> Roll number: {q}</h5>")

def ht(t):
	return render(t,'sample.html')

def mw(h,y):
	return render(h,'test.html',{'g':y})
