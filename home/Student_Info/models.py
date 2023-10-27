from django.db import models

# Create your models here.

class StudentModel2(models.Model):
    Name=models.CharField(max_length=40)
    Address=models.CharField(max_length=100)
    Number=models.IntegerField()
    Email=models.EmailField()
    Location=models.CharField(max_length=20)
    Subject=[('Python','Python'), ('Java','Java'),('Ruby','Ruby'),('Docker','Docker'),('Node','Node'),('JS','JS')]
    Tech_Skill=models.CharField(max_length=20,choices=Subject)
    Experience=models.IntegerField()
