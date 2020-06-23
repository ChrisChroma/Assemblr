from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User


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

GENRE = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JS', 'JavaScript'),
    ('UX', 'UX Design'),
    ('PI', 'Project Ideas'),
)

# =========Student Model=========
class Student(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
    # messages = models.ManyToManyField(Message)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choices
        return f"{self.name} - {self.get_cohort_display().upper()}"

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.id})




# ========= Post Model =========
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    genre = models.CharField(
        max_length=4,
        choices=GENRE,
        default=GENRE[0][0]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

    class Meta:
        ordering = ['-created_at']


# ========= Thread Model =========
class Thread(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


# ========= Message Model =========
class Message(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"From post n.{self.post_id} message id = {self.id} on {self.created_at}"

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-created_at']





