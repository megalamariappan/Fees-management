from django.db import models

class department(models.Model):
    department_name=models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.department_name

class Student(models.Model):
    regno=models.IntegerField(unique=True,null=False,blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    batch=models.CharField(max_length=20,null=True,blank=True)
    addate=models.DateField(null=False,blank=False)
    dob=models.DateField()
    dept=models.CharField(max_length=30)
    year=models.CharField(max_length=10,default='I',null=True,blank=True)
    fathername=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    contact=models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10,choices=[
        ('female','female'),
        ('male','male'),
    ])
    transport=models.CharField(max_length=20,choices=[
            ('yes','yes'),
            ('no','no'),
        ]
    )
    transport_fees=models.IntegerField(null=True,blank=False)
    hostel=models.CharField(max_length=20,choices=[
        ('yes','yes'),
        ('no','no'),
    ])
    photo=models.ImageField(upload_to='image/')
    hostel_fees=models.IntegerField(null=True,blank=True)
    pending_hostel=models.IntegerField(null=True,blank=False)
    course_fees=models.IntegerField(null=True,blank=True)
    pending_course=models.IntegerField(null=True,blank=True)
    pending_trasport=models.IntegerField(null=True,blank=True)
    total_fees=models.IntegerField(null=True,blank=True)
    total_pending=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name

class payment(models.Model):
    student_data=models.ForeignKey(Student,on_delete=models.CASCADE)
    paidamount=models.IntegerField()
    paiddate=models.DateField()
    feestype=models.CharField(max_length=50)

class CourseLevel(models.Model):
    level=models.CharField(max_length=30)
    
    def __str__(self):
        return self.level
    
class Course(models.Model):
    course_level=models.ForeignKey(CourseLevel,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30)
    full_name=models.CharField(max_length=80)
    fees=models.IntegerField()
    eligibility=models.CharField(max_length=30)
    duration=models.IntegerField()