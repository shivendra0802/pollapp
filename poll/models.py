from django.db import models
from time import timezone

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=200)
    option_three = models.CharField(max_length=255)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


