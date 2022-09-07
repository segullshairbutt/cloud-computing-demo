from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',)

