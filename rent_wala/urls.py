"""rentwala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.http import HttpResponse
app_name = 'rent_wala'

urlpatterns = [
    path('', views.home, name="home"),
    path('insta/', views.insta, name="insta"),
    path('user_info/', views.user_info, name="user_info"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('view_profile/', views.view_profile, name="view_profile"),
    path('manage_orders/', views.manage_orders, name="manage_orders"),
    path('validate/', views.validate, name="validate"),
    path('get_orders/', views.get_orders, name="get_orders"),
    path('search/', views.search, name="search"),
    # re_path(r'^validate_phone/', views.ValidatePhoneSendOTP.as_view()),
    path('validate_otp/', views.ValidateOTP),
    path('register/', views.Register, name='register'),
    path('checkout/', views.checkout, name='checkout'),
    path('log_in/', views.log_in, name="log_in"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('log_out/', views.log_out, name="log_out"),
    path('check/', views.check, name="check"),
    path('bucket/<str:cat>/', views.bucket, name="bucket"),
    path('bucketview/<str:cat>/', views.bucketview, name="bucketview"),
    path('item_view/<str:sid>/', views.item_view, name="item_view"),
]
