
from django.contrib import admin
from django.urls import path,include
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MyApp.urls'))
]
