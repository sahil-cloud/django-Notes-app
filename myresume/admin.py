from django.contrib import admin
from .models import Notes

# Register your models here.
@admin.register(Notes)
class Note(admin.ModelAdmin):
    list_display = ['id','title','desc']