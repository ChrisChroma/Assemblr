from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


PROGRAMS = (
    ('s', 'Software Engineer'),
    ('u', 'UX Design'),
)
COHORTS = (
    ('ATX', 'Austin'),
    ('DAL', 'Dallas'),
    ('LAN', 'Los Angeles'),
    ('SAN', 'San Diego'),
    ('DEN', 'Denver'),
)

SKILLS = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JS', 'JavaScript'),
    ('UX', 'UX Design'),
    ('PI', 'Project Ideas'),
)

# =========Student Model=========
class Student(models.Model):
    name = models.CharField(max_length=50)

    cohort = models.CharField(
        max_length=3,
        choices=COHORTS,
        default=COHORTS[0][0]
    )
    program = models.CharField(
        max_length=1,
        choices=PROGRAMS,
        default=PROGRAMS[0][0]
    )

    def __str__(self):
        return f"{self.name} - {self.get_cohort_display().upper()}"

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.id})




# ========= Post Model =========
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    skill = models.CharField(
        max_length=4,
        choices=SKILLS,
        default=SKILLS[0][0]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

    class Meta:
        ordering = ['-created_at']
    
# ========= Message Model =========
class Message(models.Model):
    comment = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"message id = {self.id} on {self.created_at}"

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-created_at']


