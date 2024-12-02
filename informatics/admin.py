from django.contrib import admin
from .models import Course, TextContent, DocumentContent, Semester

# Register your models here.
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(TextContent)
admin.site.register(DocumentContent)