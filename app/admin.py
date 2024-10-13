# app/admin.py

from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'city', 'email')  # Display these fields in the list view
    search_fields = ('name', 'email')  # Add a search bar for these fields
    list_filter = ('city',)  # Add a filter sidebar for this field
