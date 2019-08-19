from django.contrib import admin
from .models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "updated")
    prepopulated_fields = {"slug": ("title",), }

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

