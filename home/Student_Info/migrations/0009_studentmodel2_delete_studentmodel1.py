# Generated by Django 4.1.4 on 2023-10-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_Info', '0008_studentmodel1_delete_student_model1'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Address', models.CharField(max_length=100)),
                ('Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Location', models.CharField(max_length=20)),
                ('Tech_Skill', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('Ruby', 'Ruby'), ('Docker', 'Docker'), ('Node', 'Node'), ('JS', 'JS')], max_length=20)),
                ('Experience', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='StudentModel1',
        ),
    ]
