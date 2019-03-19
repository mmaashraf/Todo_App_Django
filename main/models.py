from django.db import models

# Create your models here.

from django.utils import timezone
import datetime

from django.http import request
from django.contrib.auth import get_user_model


from django import forms

def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
def get_now2():
    return datetime.datetime.now()


COLOR_CHOICES = (
    ('yes','YES'),
    ('no','NO'),
)

YES_NO=('COMLPLETED','NOT ')
# Create your models here.
User=get_user_model()
class MainTodo(models.Model):
    todo_deadline = models.DateTimeField(default=get_now2)
    #todo_deadline = models.DateTimeField(datetime.datetime.now())
    todo_title = models.CharField(max_length=200)
    todo_content = models.TextField()
    #todo_status = models.CharField(max_length=10)
    todo_status = models.CharField(max_length=3, choices=COLOR_CHOICES, default='no')
    todo_username = models.ForeignKey(User, on_delete=models.CASCADE,default=3)
