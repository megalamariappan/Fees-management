from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Student,department,Course,CourseLevel,payment
from django.contrib.auth import authenticate,logout,login
from django.db.models import Q,Sum
import datetime
from django.utils import timezone
# Create your views here.

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_validate=authenticate(username=username,password=password)
        if user_validate is not None:
            login(request,user_validate)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('login')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    std=Student.objects.all()
    pay=payment.objects.all()
    tot_std=len(std)
    paid_fees=0
    for i in pay:
        paid_fees+=i.paidamount
    tution_pending=hostel_pending=transport_pending=0
    for i in std:
        tution_pending+=i.pending_course
        hostel_pending+=i.pending_hostel
        transport_pending+=i.pending_trasport
    tot_pending=tution_pending+hostel_pending+transport_pending
    current_date=datetime.datetime.now().date()
    get_paydate=payment.objects.filter(paiddate=current_date)
    return render(request,'dashboard.html',{'daypayment':get_paydate,'tot_std':tot_std,'tot_paid':paid_fees,'tot_pending':tot_pending})

def stdDetails(request):
    depts=department.objects.all()
    getdept=request.GET.get('getdept')
    getname=request.GET.get('searchstd')
    if getdept and getname:
        sdetails=Student.objects.filter(name__icontains=getname,dept=getdept)
    elif getdept:
        sdetails=Student.objects.filter(dept=getdept)
    elif getname:
        sdetails=Student.objects.filter(name__icontains=getname)
    else:
        sdetails=Student.objects.all()
    return render(request,'stdDetails.html',{
                                            'depts':depts,
                                            'selected_d':getdept,
                                            'gname':getname,
                                            'stddetails':sdetails
                                            })

def addStd(request):
    departments=department.objects.all()
    courses=Course.objects.all()
    if request.method=='POST':
        regno=request.POST.get('regno')
        if not Student.objects.filter(regno=regno).exists():     
            name=request.POST.get('name')
            addate=request.POST.get('addate')
            dob=request.POST.get('dob')
            gender=request.POST.get('gender')
            dept=request.POST.get('dept')
            father_name=request.POST.get('fname')
            address=request.POST.get('address')
            contact=request.POST.get('contact')
            email=request.POST.get('email')
            transport=request.POST.get('transport')
            trans_lower=transport.lower()
            dept_lower=dept.lower()
            if trans_lower == 'yes':
                transport_fees=request.POST.get('transportfees')
            else:
                transport_fees=0
            hostel=request.POST.get('hostel')
            hostel_lower=hostel.lower()
            if hostel_lower == 'yes':
                hostel_fees=65000
            else:
                hostel_fees=0
            course_fees=0
            for i in courses:
                if dept_lower.startswith(i.course_name.lower()):
                    course_fees=i.fees
                    break
            photo=request.FILES.get('photo')
            total_fees=int(transport_fees)+int(course_fees)+int(hostel_fees)
                        
            current=datetime.datetime.now()
            current_date=current.date()
            entered_date = timezone.datetime.strptime(addate, '%Y-%m-%d').date()
            diff_date=(current_date-entered_date).days
            year1=365
            year2=year1*2
            year3=year2*3
            addate_year=entered_date.year
            if dept[0]=='M':
                batch=str(addate_year)+'-'+str(addate_year+2)
                if diff_date>year2:
                    year='Passed Out!!'
                elif diff_date>year1:
                    year='II'
                else:
                    year='I'
            else:
                batch=str(addate_year)+'-'+str(addate_year+3)
                if diff_date>year3:
                    year='Passed Out!!'
                elif diff_date>year2:
                    year='III'
                elif diff_date>year1:
                    year='II'
                else:
                    year='I'
            std_obj=Student.objects.create(
                regno=regno,
                name=name,
                addate=addate,
                dob=dob,
                gender=gender,
                dept=dept,
                fathername=father_name,
                address=address,
                year=year,
                batch=batch,
                contact=contact,
                email=email,
                transport=transport,
                transport_fees=transport_fees,
                hostel=hostel,
                hostel_fees=hostel_fees,
                course_fees=course_fees,
                pending_course=course_fees,
                pending_hostel=hostel_fees,
                pending_trasport=transport_fees,
                photo=photo,
                total_fees=total_fees,
            )
            std_obj.save()
            messages.success(request,'Successfully Added....!')
            return redirect('addStd')
        else:
            messages.error(request,'Register number must be Unique or Student already exist...!')
            return redirect('addStd')
    return render(request,'addStd.html',{'depts':departments})

def editStd(request,id):
    dept=department.objects.all()
    detail=Student.objects.get(id=id)
    courses=Course.objects.all()
    if request.method == 'POST':
        regno=request.POST.get('regno')
        name=request.POST.get('name')
        addate=request.POST.get('addate')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        dep=request.POST.get('dept')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        transport=request.POST.get('transport')
        trans_lower=transport.lower()
        dep_lower=dep.lower()
        if trans_lower == 'yes':
            transport_fees=request.POST.get('transportfees')
        else:
            transport_fees=0
        hostel=request.POST.get('hostel')
        hostel_lower=hostel.lower()
        if hostel_lower == 'yes':
            hostel_fees=65000
        else:
            hostel_fees=0
        course_fees=0
        for i in courses:
            if dep_lower.startswith(i.course_name.lower()):
                course_fees=i.fees
                break
        total_fees=int(transport_fees)+int(course_fees)+int(hostel_fees)
        photo=request.FILES.get('photo')
        
        current=datetime.datetime.now()
        current_date=current.date()
        entered_date = timezone.datetime.strptime(addate, '%Y-%m-%d').date()
        diff_date=(current_date-entered_date).days
        year1=365
        year2=year1*2
        year3=year2*3
        addate_year=entered_date.year
        if dept[0]=='M':
            batch=str(addate_year)+'-'+str(addate_year+2)
            if diff_date>year2:
                year='Passed Out!!'
            elif diff_date>year1:
                year='II'
            else:
                year='I'
        else:
            batch=str(addate_year)+'-'+str(addate_year+3)
            if diff_date>year3:
                year='Passed Out!!'
            elif diff_date>year2:
                year='III'
            elif diff_date>year1:
                year='II'
            else:
                year='I'
        
        detail.regno=regno
        detail.name=name
        detail.addate=addate
        detail.dob=dob
        detail.gender=gender
        detail.dept=dep
        detail.fathername=fname
        detail.address=address
        detail.contact=contact
        detail.email=email
        detail.transport=transport
        detail.transport_fees=transport_fees
        detail.hostel=hostel
        detail.hostel_fees=hostel_fees
        detail.batch=batch
        detail.year=year
        detail.photo=photo
        detail.course_fees=course_fees
        detail.pending_course=course_fees
        detail.pending_hostel=hostel_fees
        detail.pending_trasport=transport_fees
        detail.total_fees=total_fees
        detail.save()
        return redirect('stdDetails')
    
    return render(request,'editStd.html',{'i':detail,'dept':dept})

def deleteStd(request,id):
    getstd=Student.objects.get(id=id)
    getstd.delete()
    return redirect('stdDetails')

def courseDetails(request):
    courses=Course.objects.all()
    return render(request,'courseDetails.html',{'course':courses})

def feePayment(request):
    search=request.GET.get('searchstd')
    if search:
        std=Student.objects.filter(name__iexact=search.lower())
    else:
        std=Student.objects.all()
    
    return render(request,'feePayment.html',{'std':std,'searchname':search})
       
def feeReport(request):
    depts=department.objects.all()
    getdep=request.GET.get('getdep')
    if getdep:
        details=Student.objects.filter(dept=getdep)
    else:
        details=Student.objects.all()
    return render(request,'feeReport.html',{'depts':depts,'details':details,'getdep':getdep})

def totStd(request):
    getname=request.GET.get('namesearch')
    if getname:
        filter_name=Student.objects.filter(name__iexact=getname.lower())
    else:
        filter_name=Student.objects.all()
    return render(request,'totStd.html',{'stdname':getname,'namesearch':filter_name})

def paidStd(request):
    paid_name=request.GET.get('paidname')
    if paid_name:
        detail=Student.objects.filter(name__iexact=paid_name.lower(),pending_course=0,pending_trasport=0,pending_hostel=0)
    else:
        detail=Student.objects.filter(pending_course=0,pending_trasport=0,pending_hostel=0)
    return render(request,'paidStd.html',{'detail':detail,'paid_name':paid_name})

def unpaidStd(request):
    unpaidname=request.GET.get('unpaidname')
    if unpaidname:
        details=Student.objects.filter(Q(name__iexact=unpaidname.lower()) & Q(pending_course__gt=0) | Q(pending_trasport__gt=0) | Q(pending_hostel__gt=0))
    else:
        details=Student.objects.filter(Q(pending_course__gt=0)|Q(pending_trasport__gt=0)|Q(pending_hostel__gt=0))
    std_details=[]
    for student in details:
        std=payment.objects.filter(student_data=student).aggregate(total=Sum('paidamount'))['total'] or 0
        std_details.append({
            "student":student,
            "total_paid":std
            })
    return render(request,'unpaidStd.html',{'unpaidname':unpaidname,'details':std_details,})

def feesStructure(request):
    return render(request,'feesStructure.html')

def checkFees(request,id):
    std_id=Student.objects.get(id=id)
    if request.method == 'POST':
        feesamt=request.POST.get('feesamt')
        paidamt=request.POST.get('paidamt')
        paiddate=request.POST.get('paiddate')
        ftype=request.POST.get('ftype')
        paidamt=int(paidamt)
        if ftype=='Tution Fees' and paidamt<=std_id.pending_course and paidamt>0 or ftype=='Hostel Fees' and paidamt<=std_id.pending_hostel and paidamt>0 or ftype=='Transport Fees' and paidamt<=std_id.transport_fees and paidamt>0:
            payment_details=payment.objects.create(
                student_data=std_id,
                paidamount=paidamt,
                paiddate=paiddate,
                feestype=ftype   
            )
            payment_details.save()
            return redirect('checkFees',id=id)
        else:
            if paidamt<=0:
                messages.error(request,'Enter Valid Amount')
                return redirect('checkFees',id=id)
            else:
                messages.error(request,'The payment amount is cross the student Fees')
                return redirect('checkFees',id=id)
    pay_detail=payment.objects.filter(student_data=id)
    paid_tution=paid_hostel=paid_transport=0
    tution_fees=payment.objects.filter(student_data=id,feestype='Tution Fees')
    hostel_fees=payment.objects.filter(student_data=id,feestype='Hostel Fees')
    transport_fees=payment.objects.filter(student_data=id,feestype='Transport Fees')

    for i in pay_detail:
        if i.feestype=="Tution Fees":
            paid_tution+=i.paidamount
            
        if i.feestype=="Hostel Fees":
            paid_hostel+=i.paidamount
        
        if i.feestype=="Transport Fees":
            paid_transport+=i.paidamount
        
    std_id.pending_course=std_id.course_fees-paid_tution
    std_id.pending_hostel=std_id.hostel_fees-paid_hostel
    std_id.pending_trasport=std_id.transport_fees-paid_transport

    std_id.save()
    if std_id.pending_course<=0:
        course_status="Paid"
    elif std_id.pending_course==std_id.course_fees:
        course_status="Unpaid"
    else:
        course_status="Pending"
        
    if std_id.pending_trasport<=0:
        transport_status="Paid"
    elif std_id.pending_trasport==std_id.transport_fees:
        transport_status="Unpaid"
    else:
        transport_status="Pending"
    
    if std_id.pending_hostel<=0:
        hostel_status="Paid"
    elif std_id.pending_hostel==std_id.hostel_fees:
        hostel_status="Unpaid"
    else:
        hostel_status="Pending"
        
    
    return render(request,'checkFees.html',{'std_id':std_id,
                                            'request_paths': request.path,
                                            'pay_detail':pay_detail,
                                            'tution_fees':tution_fees,
                                            'transport_fees':transport_fees,
                                            'hostel_fees':hostel_fees,
                                            'paid_tution':paid_tution,
                                            'paid_hostel':paid_hostel,
                                            'paid_transport':paid_transport,
                                            "course_status":course_status,
                                            "transport_status":transport_status,
                                            "hostel_status":hostel_status,
                                            })

def addCourse(request):
    levels=CourseLevel.objects.all()
    
    if request.method=='POST':
        course_level_id=request.POST.get('level')
        course_name=request.POST.get('course_name')
        course_lower=course_name.lower()
        if not Course.objects.filter(course_name__iexact=course_lower).exists():     
            full_name=request.POST.get('ab_course')
            fees=request.POST.get('fees')
            eligibility=request.POST.get('eligible')
            duration=request.POST.get('duration')
            
            course_level=CourseLevel.objects.get(id=course_level_id)
            new_course=Course.objects.create(
                course_level=course_level,
                course_name=course_name,
                full_name=full_name,
                fees=fees,
                eligibility=eligibility,
                duration=duration
            )
            new_course.save()
            messages.success(request,'Course Added Successfully....!')
            return redirect('courseDetails')
        else:
            messages.error(request,'Course is Already Exist Please Enter Another Course...!')
            return redirect('addCourse')
    return render(request,'addCourse.html',{'levels':levels})

def addDept(request):
    if request.method=='POST':
        dept=request.POST.get('dept_name')
        lower_dept=dept.lower()
        if not department.objects.filter(department_name__iexact=lower_dept).exists():
            depts=department.objects.create(department_name=dept)
            depts.save()
            messages.success(request,'Department addedd Successfully')
            return redirect('courseDetails')
        else:
            messages.error(request,'Department already Exist...!')
            return redirect('addDept')
    return render(request,'addDept.html')