from django.contrib import admin
from django.urls import path
from MyApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('stdDetails',views.stdDetails,name='stdDetails'),
    path('courseDetails',views.courseDetails,name='courseDetails'),
    path('feePayment',views.feePayment,name='feePayment'),
    path('feeReport',views.feeReport,name='feeReport'),
    
    path('totStd',views.totStd,name='totStd'),
    path('paidStd',views.paidStd,name='paidStd'),
    path('unpaidStd',views.unpaidStd,name='unpaidStd'),
    path('feesStructure',views.feesStructure,name='feesStructure'),
    
    path('addStd',views.addStd,name='addStd'),
    
    path('checkFees/<int:id>',views.checkFees,name='checkFees'),
    
    path('addCourse',views.addCourse,name='addCourse'),
    path('addDept',views.addDept,name='addDept'),
    path('editStd/<int:id>',views.editStd,name='editStd'),
    path('deleteStd/<int:id>',views.deleteStd,name='deleteStd'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)