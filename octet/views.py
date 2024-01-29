# Create your views here.
from django.shortcuts import render,

def home(request):
    return render(request, 'octet/index.html')

def services(request):
    return render(request, 'services/services.html')

def cyber_security(request):
    return render(request, 'cybersecurity/cybersecurity.html')

# Add other view functions as needed