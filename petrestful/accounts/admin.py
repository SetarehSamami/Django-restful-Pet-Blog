from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import User as django_user


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


