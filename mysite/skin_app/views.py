from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "GET":
        return render(request,'index.html')
    
@csrf_exempt
def submit(request):
    if request.method == "POST":
        return render(request,'index.html')
    
@csrf_exempt
def logout(request):
    if request.method == 'GET':
        return redirect('http://127.0.0.1:8000')    