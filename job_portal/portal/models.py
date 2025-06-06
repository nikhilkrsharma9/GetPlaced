from django.db import models

# Create your models here.

# models for college entity
class college (models.Model):
    college_name = models.CharField(max_length = 100, default = 'N/A')
    college_location = models.CharField(max_length = 100, default = 'N/A')
    college_affiliation = models.CharField(max_length = 100, default = 'N/A')
    college_logo = models.ImageField(upload_to='college_logos/', default='college_logos/default.png')
    college_website = models.URLField(max_length=200, default='https://www.example.com')
    college_mobile_no = models.CharField(max_length=15, default='N/A')
    college_email = models.EmailField(max_length=100, default='N/A')
    college_description = models.TextField(default='N/A')
    class Meta:
        db_table = "college"
        
