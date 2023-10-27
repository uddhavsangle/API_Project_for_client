from django.contrib import admin
from .models import StudentModel2
# Register your models here.


class Stud_Admin(admin.ModelAdmin):
    class Meta:
        model=StudentModel2
        fields="__all__"
admin.site.register(StudentModel2,Stud_Admin)