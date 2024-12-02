from django.contrib import admin
from .models import Content, Course, TextContent, DocumentContent

# Register your models here.
# admin.site.register(Content)
admin.site.register(Course)
admin.site.register(TextContent)
admin.site.register(DocumentContent)