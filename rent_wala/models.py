from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db.models import Q
from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from datetime import timedelta

import random
import os
import requests


# Create your models here


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, is_admin=False):
        if not phone:
            raise ValueError("Phone required")
        if not password:
            raise ValueError("required Password")
        user_obj = self.model(
            phone=phone
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Enter Valid number")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    first_login = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone

    def get_full_name(self):
        if self.name:
            return self.name
        else:
            return self.phone

    def get_short_name(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


def file_upload_aadhar(instance, filename):
    return 'users/img/{0}/aadhar/{1}'.format(instance.phone, filename)


def file_upload_pan(instance, filename):
    return 'users/img/{0}/pan/{1}'.format(instance.phone, filename)


def profile_upload(instance, filename):
    return 'users/img/{0}/profile_pic/{1}'.format(instance.phone, filename)


class MyUser(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Enter Valid number")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    password = models.CharField(max_length=20, blank=False, null=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=False, default="")
    profile_pic = models.CharField(max_length=1000, blank=True)
    checkout_count = models.IntegerField(default=0, blank=False, null=False)
    validated = models.BooleanField(default=False, help_text="If its True user is validated.")

    def __str__(self):
        return self.phone


class UserInfo(models.Model):
    rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    password2 = models.CharField(max_length=20, blank=False, null=False)
    profile_pic = models.ImageField(upload_to=profile_upload, blank=True)
    aadhar_card = models.FileField(upload_to=file_upload_aadhar)
    pan_card = models.FileField(upload_to=file_upload_pan)
    address = models.CharField(max_length=2000, blank=False, null=True)

    def __str__(self):
        return self.phone


class PhoneOTP(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Enter Valid number")
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    otp = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(default=0, help_text="number of OTP sent")
    date = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False, help_text="If its True user is validated")

    def __str__(self):
        return str(self.phone) + 'is sent' + str(self.otp)


class Cat(models.Model):
    sid = models.CharField(max_length=100000000000000, default="", unique=True)
    title = models.CharField(max_length=1000000000, default="")
    cat = models.CharField(max_length=1000000000000, default="")
    Poster = models.CharField(max_length=1000000000000, default="")

    def __str__(self):
        return self.cat


class Product(models.Model):
    sid = models.CharField(max_length=1000000000000000000000, default="", unique=True, blank=False)
    title = models.CharField(max_length=1000000000000000, default="", blank=False)
    desc = models.CharField(max_length=500, default="", blank=False)
    subcat = models.CharField(max_length=10000, default="", blank=False)
    cat = models.CharField(max_length=10000000, default="", blank=False)
    rent_price = models.CharField(max_length=10000000, default="", blank=True, null=True)
    key1 = models.CharField(max_length=300, default="", blank=True)
    key2 = models.CharField(max_length=300, default="", blank=True)
    key3 = models.CharField(max_length=300, default="", blank=True)
    key4 = models.CharField(max_length=300, default="", blank=True)
    Poster = models.CharField(max_length=10000000, default="", blank=True)
    Poster2 = models.CharField(max_length=10000000, default="", blank=True)
    Poster3 = models.CharField(max_length=10000000, default="", blank=True)

    def __str__(self):
        return self.subcat


def order_expiry_date(instance):
    date = instance.date
    days = instance.days
    expiry_time = date + timedelta(days=days)
    return expiry_time


class Order(models.Model):
    phone = models.CharField(max_length=20, blank=False, default="")
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=1000, default="", blank=True, null=True)
    order_id = models.CharField(max_length=100000000000000000000000, default="a-1", blank=False)
    category = models.CharField(default="", max_length=500)
    received = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    handshake = models.BooleanField(default=False)

    def __str__(self):
        return self.phone


class ContactUs(models.Model):
    rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    count = models.IntegerField(default=1, blank=True, null=True)
    querry = models.CharField(max_length=1000, default="", blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)


class GetOrder(models.Model):
    rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=False, default="")
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=1000, default="", blank=True, null=True)
    quantity = models.CharField(max_length=100, default=1)
    days = models.CharField(max_length=100, default=1)
    time_left = models.CharField(max_length=1000, default=1)
    title = models.CharField(max_length=1000, default="", blank=False)
    total = models.CharField(max_length=1000000000000000000000, default="", blank=False, null=True)
    order_id = models.CharField(max_length=100000000000000000000000, default="a-1", blank=False)
    product_id = models.CharField(max_length=100000000000000000000000, default="", blank=False)
    poster = models.CharField(max_length=100000000000000000000, default="", blank=False)
    validated = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    out_for_delivery = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    handshake = models.BooleanField(default=False)

    def __str__(self):
        return self.rel.phone