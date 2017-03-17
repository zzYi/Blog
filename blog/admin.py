from django.contrib import admin
from models import *
# Register your models here.


class Blogadmin(admin.ModelAdmin):
    list_display = ("title", "clicks", "datetime")
    search_fields = ("title", "description")
    readonly_fields = ("clicks",)


class Descriptionadmin(admin.ModelAdmin):
    list_display = ("description", "text",)


admin.site.register(Blog, Blogadmin)
admin.site.register(Description, Descriptionadmin)
