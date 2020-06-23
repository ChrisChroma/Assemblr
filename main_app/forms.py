from django.forms import ModelForm
from .models import Message, Student

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'