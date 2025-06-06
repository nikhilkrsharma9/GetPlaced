from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index (request):
    return render(request, 'index.html')

def job_search(request):
    # Implement your search logic here
    return render(request, 'search_results.html')