# Generated by Django 4.0.3 on 2023-04-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultmanagementapp', '0005_delete_resultmodel_eightresultmodel_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='courses/')),
                ('title', models.CharField(max_length=250)),
                ('introduction', models.TextField()),
            ],
        ),
    ]
