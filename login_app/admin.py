from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Register your models here.
admin.site.register(Users)
class CustomUserAdmin(UserAdmin):
    add_fieldsets=UserAdmin.add_fieldsets+(
        (None,{'fields':('email')})
    )

add_form=UserCreationForm
form=UserChangeForm
model=Users
list_display=['pk','email','username']