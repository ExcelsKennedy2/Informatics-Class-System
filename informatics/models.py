from django.db import models
from django.core.validators import URLValidator
from ckeditor.fields import RichTextField
# from cloudinary.models import CloudinaryField
# import cloudinary.utils


class Course(models.Model):
    """
    Model representing a course in the class.
    """
    name = models.CharField(max_length=255, unique=True)
    whatsapp_group_invite_link = models.URLField(validators=[URLValidator], blank=True, null=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    """
    Model representing a semester (e.g., Fall 2024, Spring 2025).
    """
    name = models.CharField(max_length=255, unique=True)
    courses = models.ManyToManyField(Course, blank=True)  # ManyToMany relationship with Course

    def __str__(self):
        return self.name

class ContentManager(models.Manager):
    def get_all_for_course(self, course_name):
        return self.filter(course__name=course_name)

class Content(models.Model):
    """
    Model representing different types of content (notes, CATs, assignments).
    """
    TYPE_CHOICES = (
        ('NOTE', 'Note'),
        ('CAT', 'CAT'),
        ('ASSIGNMENT', 'Assignment'),
    )
    content_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='NOTE')

    # Common fields for all content types
    title = models.CharField(max_length=255)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    objects = ContentManager()

    class Meta:
        abstract = True

class DocumentContent(Content):
    """
    Model for content uploaded as documents.
    """
    file = models.FileField(upload_to='documents/')
    name = models.CharField(max_length=255, default='document')

    def __str__(self):
        return self.name
#
#     # test
#     file = CloudinaryField(
#         'file',
#         resource_type='raw',
#         overwrite=True
#     )
#     # name = models.CharField(max_length=255, default='document')
#
#     # def __str__(self):
#     #     return self.name
#     #
#     def get_download_url(self):
#         url, options = cloudinary.utils.cloudinary_url(
#             self.file.public_id,
#             resource_type="raw",
#             type="upload",
#             secure=True,
#             flags="attachment"  # This forces the file to download
#         )
#         return self.name
#
#     def __str__(self):
#         return self.name
# class DocumentContent(Content):
#     """
#     Model for content uploaded as documents.
#     """
#     file = CloudinaryField(
#         'file',
#         resource_type='raw',
#         overwrite=True
#     )
#     name = models.CharField(max_length=255, default='document')
#
#     def get_download_url(self):
#         url, options = cloudinary.utils.cloudinary_url(
#             self.file.public_id,
#             resource_type="raw",
#             type="upload",
#             secure=True,
#             flags="attachment"  # This forces the file to download
#         )
#         return url  # Return the generated URL
#
#     def __str__(self):
#         return self.name

# from django.db import models # Assuming Content model is in the same app or a 'content' app
# from cloudinary.models import CloudinaryField
# import cloudinary.utils
#
# class DocumentContent(Content):
#     """
#     Model for content uploaded as documents using Cloudinary.
#     """
#     file = CloudinaryField(
#         'document',  # Human-readable name for the field
#         resource_type='raw',
#         overwrite=True,
#         folder='documents'  # Optional: Specify a folder in Cloudinary
#     )
#     name = models.CharField(max_length=255, default='document')
#
#     def __str__(self):
#         return self.name

    # def get_download_url(self):
    #     """
    #     Generates a secure URL for downloading the document.
    #     """
    #     url, options = cloudinary.utils.cloudinary_url(
    #         self.file.public_id,
    #         resource_type="raw",
    #         type="upload",
    #         secure=True,
    #         flags="attachment"  # Forces the browser to download the file
    #     )
    #     return url

class TextContent(Content):
    """
    Model for content typed out directly.
    """
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.content_type})"

class Event(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='events/')
    description = RichTextField(blank=False, null=False)
    day = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.name