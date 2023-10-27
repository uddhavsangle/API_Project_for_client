from django.shortcuts import render,HttpResponseRedirect
from rest_framework.filters import SearchFilter
from rest_framework import filters
from  .models import StudentModel2
from .Serializer import studser1
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.paginator import Paginator
from django.http import JsonResponse
import boto3
import json

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os
import  copy
# Create your views here.

class api_view(APIView):
    def get(self,r):
        filter_field = r.GET.get('filter_field', None)
        filter_value = r.GET.get('filter_value', None)
        page = r.GET.get('page', 1)
        items_per_page = r.GET.get('items_per_page', 10)

        queryset = StudentModel2.objects.all()

        if filter_field and filter_value:
            queryset = queryset.filter(**{filter_field: filter_value})

        paginator = Paginator(queryset, items_per_page)

        try:
            paginated_data = paginator.page(page)
        except 'empty data':
            return JsonResponse({'message': 'Page not found'}, status=404)

        data = [{'id':item.id,'Name':item.Name,'Address':item.Address,'Number':item.Number,'Email':item.Email,'Tech_Skill': item.Tech_Skill, 'Location': item.Location,'Experience':item.Experience} for item in paginated_data]

        sr = studser1(data, many=True)
        return Response(sr.data)



    def post(self,r):
        srobj=studser1(data=r.data,many=True)
        if srobj.is_valid():
            srobj.save()
            for i in srobj.data:

                id=i.get('id')
                name=i.get('Name')
                address = i.get('Address')
                number = i.get('Number')
                email = i.get('Email')
                location = i.get('Location')
                tech_skill = i.get('Tech_Skill')
                yoe=i.get('Experience')

                with open('resume.txt','r+')as resume_format:
                    text = resume_format.read().format(name,number,tech_skill,tech_skill,tech_skill,yoe,tech_skill,tech_skill,tech_skill,tech_skill,name)

                with open('sample.txt','w') as data_text:
                    data_text.write(text)


                def text_to_pdf(text_file, pdf_file):
                    doc = SimpleDocTemplate(pdf_file, pagesize=letter)

                    # Create a list to hold the flowables (elements to be added to the PDF)
                    story = []

                    # Create a style for the text
                    styles = getSampleStyleSheet()
                    style = styles["Normal"]

                    # Open the text file and read its content
                    with open(text_file, "r") as file:
                        text_content = file.read()

                    # Create a Paragraph and add it to the story paragrap
                        # Create a Paragraph and add it to the story
                    paragraph = Paragraph(text_content, style)
                    story.append(paragraph)

                    # Build the PDF document
                    doc.build(story)

                output_file = str(id) + '.pdf'
                path1 = r"C:\Users\Lenovo\Desktop\pdf"
                path2 = output_file
                result_path = os.path.join(path1, path2)
                text_file = "sample.txt"
                # Convert the text file to a PDF
                text_to_pdf(text_file, result_path)

                print(f"Text file '{text_file}' has been converted to PDF: '{result_path}'")

                session = boto3.Session(
                    aws_access_key_id='',
                    aws_secret_access_key='',
                    region_name='ap-south-1'
                )

                s3 = session.client('s3')
                s3.upload_file(result_path,'apitrigerdata',output_file)


            return Response(srobj.data,status=status.HTTP_201_CREATED)
        return Response(srobj.errors,status=status.HTTP_400_BAD_REQUEST)
class api_change(APIView):
    def put(self,r,id):
        ob=StudentModel2.objects.get(id=id)
        sro = studser1(ob,data=r.data)
        if sro.is_valid():
            sro.save()
            return Response(sro.data,status=status.HTTP_201_CREATED)
        return Response(sro.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,id):
        ob = StudentModel2.objects.get(id=id)
        ob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






#http://127.0.0.1:8000/get/?page=2&items_per_page=5                                   # only for page wise search

# http://127.0.0.1:8000/get/?filter_field=Tech_Skill&filter_value=Python&items_per_page=10          #for search and item per

