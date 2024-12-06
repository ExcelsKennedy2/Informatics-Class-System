from django.db import models
from django.core.validators import URLValidator

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

class TextContent(Content):
    """
    Model for content typed out directly.
    """
    text = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.content_type})"

class Event(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='events/')
    description = models.TextField(blank=False, null=False)
    day = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.name