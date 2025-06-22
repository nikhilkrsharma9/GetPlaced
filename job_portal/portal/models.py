from django.db import models
from django.contrib.auth.hashers import make_password, is_password_usable

# Create your models here.

# models for college entity
class college (models.Model):
    college_name = models.CharField(max_length = 100, default = 'N/A')
    college_location = models.CharField(max_length = 100, default = 'N/A')
    college_university = models.CharField(max_length = 100, default = 'N/A')
    college_logo = models.ImageField(upload_to='college_logos/', default='college_logos/default.png')
    college_website = models.URLField(max_length=200, default='https://www.example.com')
    college_mobile_no = models.CharField(max_length=15, default='N/A')
    college_email = models.EmailField(max_length=100, default='N/A')
    college_description = models.TextField(default='N/A')
    college_registration_id = models.CharField(max_length=20, default='N/A')
    college_registration_password = models.CharField(max_length=128, default='N/A')  # Increase length for hashes
    admin_verified = models.BooleanField(default=False)
    college_rating = models.PositiveSmallIntegerField(default=0, help_text="Rating (1-5 stars)")
    

    def __str__(self):
        return self.college_name
    
    class Meta:
        db_table = "college"
        
class student (models.Model):
    student_name = models.CharField(max_length = 100, default = 'N/A')
    student_reg_no = models.CharField(max_length = 20, default = 'N/A')
    student_branch = models.CharField(max_length = 50, default = 'N/A')
    student_year = models.CharField(max_length = 20, default = 'N/A')
    student_skills = models.CharField(max_length = 20, default = 'N/A')
    student_image = models.ImageField(upload_to='student_images/', default='student_images/default.png')
    student_mobile_no = models.CharField(max_length=15, default='N/A')
    student_email = models.EmailField(max_length=100, default='N/A')
    college = models.ForeignKey(college, on_delete=models.CASCADE, related_name='students', default=1)

    def __str__(self):
        return self.student_name

    class Meta:
        db_table = "student"

class company (models.Model):
    company_name = models.CharField(max_length = 100, default = 'N/A')
    company_location = models.CharField(max_length = 100, default = 'N/A')
    company_logo = models.ImageField(upload_to='company_logos/', default='company_logos/default.png')
    company_website = models.URLField(max_length=200, default='https://www.example.com')
    company_mobile_no = models.CharField(max_length=15, default='N/A')
    company_email = models.EmailField(max_length=100, default='N/A')
    company_description = models.TextField(default='N/A')
    company_registration_id = models.CharField(max_length=20, default='N/A')
    company_registration_password = models.CharField(max_length=128, default='N/A')  # Increase length for hashes
    admin_verified = models.BooleanField(default=False)
    company_rating = models.PositiveSmallIntegerField(default=0, help_text="Rating (1-5 stars)")
    

    def __str__(self):
        return self.company_name
    
    class Meta:
        db_table = "company"

class job(models.Model):
    job_title = models.CharField(max_length=100, default='N/A')
    job_description = models.TextField(default='N/A')
    job_location = models.CharField(max_length=100, default='N/A')
    job_type = models.CharField(max_length=50, default='Full Time')  # e.g., Full Time, Part Time, Internship
    job_skills_required = models.CharField(max_length=100, default='N/A')
    job_salary = models.CharField(max_length=50, default='N/A')
    job_posted_on = models.DateField(auto_now_add=True)
    job_last_date = models.DateField(null=True, blank=True)
    job_contact_email = models.EmailField(max_length=100, default='N/A')
    company = models.ForeignKey(company, on_delete=models.CASCADE, related_name='jobs', default=1)

    def __str__(self):
        return self.job_title

    class Meta:
        db_table = "job"

class ticket(models.Model):
    college = models.ForeignKey(college, on_delete=models.CASCADE, related_name='tickets')
    company = models.ForeignKey(company, on_delete=models.CASCADE, related_name='tickets')
    message = models.TextField(default='No message provided')
    status = models.CharField(max_length=20, default='pending')  # pending, connect, approved, rejected, cancelled
    is_active = models.BooleanField(default=True)
    requested_by = models.CharField(max_length=100, default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket: {self.college.college_name} -> {self.company.company_name} ({self.status})"

    class Meta:
        db_table = 'ticket'
        unique_together = ('college', 'company', 'is_active')

class ChatMessage(models.Model):
    ticket = models.ForeignKey(ticket, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=20)  # 'College' or 'Company'
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.text[:30]}..."

    class Meta:
        db_table = 'chat_message'