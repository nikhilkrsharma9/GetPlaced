from django.contrib import admin
from .models import college,company,student,job
# Register your models here.


admin.site.register(college)
admin.site.register(company)
admin.site.register(student)
admin.site.register(job)