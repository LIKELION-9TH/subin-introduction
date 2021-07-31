from django.db import models

# Create your models here.
class Visit(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.name