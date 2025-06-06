from django.db import models

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
    
    def __str__(self):
        return self.student_name
    
    class Meta:
        db_table = "student"
        
