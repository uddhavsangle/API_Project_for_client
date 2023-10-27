from rest_framework import serializers
from .models import StudentModel2

class studser1(serializers.ModelSerializer):
    class Meta:
        model=StudentModel2
        fields="__all__"