from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.
PROGRAMS = (
    ('s', 'Software Engineer'),
    ('u', 'UX Design'),
)
COHORTS = (
    ('atx', 'Austin'),
    ('dal', 'Dallas'),
    ('lan', 'Los Angeles'),
    ('san', 'San Diego'),
    ('den', 'Denver'),
)
#=========Post Model=========
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date = models.DateField('Post Date')
    #Maybe add a genre???

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


#=========Message Model=========
class Message(models.Model):
    content = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    date = models.DateField('Message Date')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']



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
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_cohort_display()}" f"{self.get_program_display()}"


    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})