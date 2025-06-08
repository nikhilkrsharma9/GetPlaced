from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import college, company
from django.contrib.auth.hashers import make_password, check_password

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
            college_registration_id=data.get('college_registration_id'),
            college_registration_password=data.get('college_registration_password'),
        )
        submitted = True
    return render(request, 'college_register.html', {'submitted': submitted})

def college_login(request):
    popup_message = None
    if request.method == 'POST':
        reg_id = request.POST.get('college_registration_id')
        password = request.POST.get('college_registration_password')
        try:
            college_obj = college.objects.get(college_registration_id=reg_id)
            if password == college_obj.college_registration_password:
                if college_obj.admin_verified:
                    # Login successful (you can set session here)
                    return render(request, 'index.html', {'college': college_obj})
                else:
                    popup_message = "Wait for admin verification."
            else:
                popup_message = "Invalid input credentials."
        except college.DoesNotExist:
            popup_message = "College does not exist"
    return render(request, 'college_login.html', {'popup_message': popup_message})

def company_register(request):
    submitted = False
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        company.objects.create(
            company_name=data.get('company_name'),
            company_location=data.get('company_location'),
            company_logo=files.get('company_logo'),
            company_website=data.get('company_website'),
            company_mobile_no=data.get('company_mobile_no'),
            company_email=data.get('company_email'),
            company_description=data.get('company_description'),
            company_registration_id=data.get('company_registration_id'),
            company_registration_password=data.get('company_registration_password'),
        )
        submitted = True
    return render(request, 'company_register.html', {'submitted': submitted})

def company_login(request):
    popup_message = None
    if request.method == 'POST':
        reg_id = request.POST.get('company_registration_id')
        password = request.POST.get('company_registration_password')
        try:
            company_obj = company.objects.get(company_registration_id=reg_id)
            if password == company_obj.company_registration_password:
                if company_obj.admin_verified:
                    return render(request, 'index.html', {'company': company_obj})
                else:
                    popup_message = "Wait for admin verification."
            else:
                popup_message = "Invalid input credentials."
        except company.DoesNotExist:
            popup_message = "Company does not exist"
    return render(request, 'company_login.html', {'popup_message': popup_message})

