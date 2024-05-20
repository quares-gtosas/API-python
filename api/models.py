from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Task(models.Model):
    task_desc = models.CharField(max_length=2000)
    task_title = models.CharField(max_length=200)
    estimation_hour = models.IntegerField()
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title
