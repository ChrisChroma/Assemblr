from django.contrib import admin
from .models import Post, Student, Message


# Register your models here.
admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Message)