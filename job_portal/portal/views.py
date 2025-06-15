from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import college, company, student, job
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

# it is the index or home page
def index (request):
    sample_colleges = college.objects.filter(admin_verified=True)[:3]
    sample_companies = company.objects.filter(admin_verified=True)[:3]
    return render(request, 'index.html', {
        'sample_colleges': sample_colleges,
        'sample_companies': sample_companies,
    })

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
                    # Redirect to dashboard after login
                    return redirect('college_after_login', college_id=college_obj.id)
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
                    return redirect('company_after_login', company_id=company_obj.id)
                else:
                    popup_message = "Wait for admin verification."
            else:
                popup_message = "Invalid input credentials."
        except company.DoesNotExist:
            popup_message = "Company does not exist"
    return render(request, 'company_login.html', {'popup_message': popup_message})

def college_list(request):
    query = request.GET.get('q', '')
    colleges = college.objects.filter(admin_verified=True)
    if query:
        colleges = colleges.filter(college_name__icontains=query)
    colleges = colleges.order_by('-college_rating', 'college_name')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'college_list_results.html', {'colleges': colleges})
    return render(request, 'college_list.html', {'colleges': colleges})

def company_list(request):
    query = request.GET.get('q', '')
    companies = company.objects.filter(admin_verified=True)
    if query:
        companies = companies.filter(company_name__icontains=query)
    companies = companies.order_by('-company_rating', 'company_name')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'company_list_results.html', {'companies': companies})
    return render(request, 'company_list.html', {'companies': companies})

def college_after_login(request, college_id):
    college_obj = get_object_or_404(college, id=college_id)
    students = student.objects.filter(college=college_obj)
    action = request.GET.get('action')
    student_id = request.GET.get('student_id')
    context = {'college': college_obj, 'students': students}

    if action == 'edit' and student_id:
        student_to_edit = get_object_or_404(student, id=student_id, college=college_obj)
        context['action'] = 'edit'
        context['student_to_edit'] = student_to_edit
        if request.method == 'POST':
            student_to_edit.student_name = request.POST.get('student_name')
            student_to_edit.student_reg_no = request.POST.get('student_reg_no')
            student_to_edit.student_branch = request.POST.get('student_branch')
            student_to_edit.student_year = request.POST.get('student_year')
            student_to_edit.student_skills = request.POST.get('student_skills')
            student_to_edit.student_email = request.POST.get('student_email')
            if request.FILES.get('student_image'):
                student_to_edit.student_image = request.FILES['student_image']
            student_to_edit.save()
            return redirect('college_after_login', college_id=college_obj.id)
    elif action == 'delete' and student_id:
        student_to_delete = get_object_or_404(student, id=student_id, college=college_obj)
        context['action'] = 'delete'
        context['student_to_delete'] = student_to_delete
        if request.method == 'POST':
            student_to_delete.delete()
            return redirect('college_after_login', college_id=college_obj.id)
    return render(request, 'college_after_login.html', context)

def add_student(request, college_id):
    college_obj = college.objects.get(id=college_id)
    if request.method == 'POST':
        data = request.POST
        student.objects.create(
            student_name=data.get('student_name'),
            student_reg_no=data.get('student_reg_no'),
            student_branch=data.get('student_branch'),
            student_year=data.get('student_year'),
            student_skills=data.get('student_skills'),
            student_image=request.FILES.get('student_image'),
            student_mobile_no=data.get('student_mobile_no'),
            student_email=data.get('student_email'),
            college=college_obj
        )
        return redirect('college_after_login', college_id=college_id)
    return render(request, 'add_student.html', {'college': college_obj})

def company_after_login(request, company_id):
    company_obj = company.objects.get(id=company_id)
    jobs = job.objects.filter(company=company_obj)
    action = request.GET.get('action')
    job_id = request.GET.get('job_id')
    context = {'company': company_obj, 'jobs': jobs}

    if action == 'edit' and job_id:
        job_to_edit = get_object_or_404(job, id=job_id, company=company_obj)
        context['action'] = 'edit'
        context['job_to_edit'] = job_to_edit
        if request.method == 'POST':
            job_to_edit.job_title = request.POST.get('job_title')
            job_to_edit.job_description = request.POST.get('job_description')
            job_to_edit.job_location = request.POST.get('job_location')
            job_to_edit.job_type = request.POST.get('job_type')
            job_to_edit.job_skills_required = request.POST.get('job_skills_required')
            job_to_edit.job_salary = request.POST.get('job_salary')
            job_to_edit.job_last_date = request.POST.get('job_last_date')
            job_to_edit.job_contact_email = request.POST.get('job_contact_email')
            job_to_edit.save()
            return redirect('company_after_login', company_id=company_obj.id)
    elif action == 'delete' and job_id:
        job_to_delete = get_object_or_404(job, id=job_id, company=company_obj)
        context['action'] = 'delete'
        context['job_to_delete'] = job_to_delete
        if request.method == 'POST':
            job_to_delete.delete()
            return redirect('company_after_login', company_id=company_obj.id)
    return render(request, 'company_after_login.html', context)

def add_job(request, company_id):
    company_obj = company.objects.get(id=company_id)
    if request.method == 'POST':
        data = request.POST
        job.objects.create(
            job_title=data.get('job_title'),
            job_description=data.get('job_description'),
            job_location=data.get('job_location'),
            job_type=data.get('job_type'),
            job_skills_required=data.get('job_skills_required'),
            job_salary=data.get('job_salary'),
            job_last_date=data.get('job_last_date'),
            job_contact_email=data.get('job_contact_email'),
            company=company_obj
        )
        return redirect('company_after_login', company_id=company_id)
    return render(request, 'add_job.html', {'company': company_obj})

# Add edit_job and delete_job views as needed

