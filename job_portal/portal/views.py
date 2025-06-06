from django.http import HttpResponse
from django.shortcuts import render, redirect

# it is the index or home page
def index (request):
    return render(request, 'index.html')

#it is the search box in index.html or home page
def job_search(request):
    return render(request, 'search_results.html')