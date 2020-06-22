from django.db import models
from django.urls import reverse

from django.utils import timezone



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
#=========Post Model=========
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    # created = models.DateTimeField(auto_now_add=True)
    created = timezone.now()

    genre = models.CharField(
        max_length=4,
        choices=GENRE,
        default=GENRE[0][0]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

    # class Meta:
    #     ordering = ['-date']

#=========Message Model=========

class Message(models.Model):
    content = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
    created = timezone.now()

    def __str__(self):
        return f"From {self.post} on {self.created}"

    # class Meta:
    #     ordering = ['-date']


#========= Reply Model=========
class Reply(models.Model):
    title = models.CharField(max_length=100)
    post = models.ForeignKey(Message, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True)
    created = timezone.now()

    def __str__(self):
        return f"From {self.post} on {self.created}"

    # class Meta:
    #     ordering = ['-date']

#=========Student Model=========
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
    messages = models.ManyToManyField(Message)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choices
        return f"{self.name} - {self.get_cohort_display().upper()}"


    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.id})