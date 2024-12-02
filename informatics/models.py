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

    def __str__(self):
        return self.name

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

    class Meta:
        abstract = True

class DocumentContent(Content):
    """
    Model for content uploaded as documents.
    """
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.title} ({self.content_type})"

class TextContent(Content):
    """
    Model for content typed out directly.
    """
    text = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.content_type})"