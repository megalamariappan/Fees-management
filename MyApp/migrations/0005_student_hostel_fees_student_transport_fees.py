# Generated by Django 5.1.1 on 2024-09-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_course_course_name_course_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hostel_fees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='transport_fees',
            field=models.IntegerField(null=True),
        ),
    ]
