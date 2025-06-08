from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import college

# it is the index or home page
def index (request):
    return render(request, 'index.html')

#it is the search box in index.html or home page
def job_search(request):
    return render(request, 'search_results.html')

def college_register(request):
    submitted = False
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        college.objects.create(
            college_name=data.get('college_name'),
            college_location=data.get('college_location'),
            college_university=data.get('college_university'),
            college_logo=files.get('college_logo'),
            college_website=data.get('college_website'),
            college_mobile_no=data.get('college_mobile_no'),
            college_email=data.get('college_email'),
            college_description=data.get('college_description'),
        )
        submitted = True
    return render(request, 'college_register.html', {'submitted': submitted})

def college_register_success(request):
    return render(request, 'college_register_success.html')