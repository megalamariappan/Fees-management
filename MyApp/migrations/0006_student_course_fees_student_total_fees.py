# Generated by Django 5.1.1 on 2024-09-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_student_hostel_fees_student_transport_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_fees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='total_fees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
