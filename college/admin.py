# -*- coding: utf-8 -*-
"""
    this is admin module for our college app
"""
from __future__ import unicode_literals

from django.contrib import admin
from college.models import StudentApplication, StudentRegistration, StaffRegistration, Department

# Register your models here.


class StudentApplicationAdmin(admin.ModelAdmin):
    """
        here we are extending the admin user interface.
    """
    list_display = ['id', 'student_name', 'email', 'dob']


admin.site.register(StudentApplication, StudentApplicationAdmin)
admin.site.register(StudentRegistration)
admin.site.register(StaffRegistration)
admin.site.register(Department)
