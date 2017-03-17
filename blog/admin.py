from django.contrib import admin
from models import *
# Register your models here.


class Blogadmin(admin.ModelAdmin):
    list_display = ("title", "description", "clicks", "datetime")
    search_fields = ("title", "description")
    readonly_fields = ("clicks",)


admin.site.register(Blog, Blogadmin)
admin.site.register(Description)
