from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    id = models.PositiveIntegerField(primary_key=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    STATUS_CHOICES = [
        (1, 'Open/Not Done'),
        (2, 'Completed')
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title