# Generated by Django 4.2.6 on 2023-10-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Address', models.CharField(max_length=100)),
                ('Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Location', models.CharField(max_length=20)),
                ('Tech_Skill', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('Ruby', 'Ruby'), ('Docker', 'Docker'), ('Node', 'Node'), ('JS', 'JS')], max_length=20)),
            ],
        ),
    ]
