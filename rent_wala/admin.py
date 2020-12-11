from __future__ import unicode_literals

from django.contrib import admin
from .models import Cat, Product, PhoneOTP, UserInfo, MyUser, Order, ContactUs, GetOrder
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = ('name', 'phone', 'admin',)
    list_filter = ('staff', 'active', 'admin',)
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('phone', 'password1', 'password2')}),
    )
    search_fields = ('phone', 'name', 'order_id')
    ordering = ('phone', 'name')
    filter_horizontal = ()

    # inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(Cat)
admin.site.register(Order)
admin.site.register(MyUser)
admin.site.register(UserInfo)
admin.site.register(Product)
admin.site.register(PhoneOTP)
admin.site.register(ContactUs)
admin.site.register(GetOrder)
