from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    github_id = models.IntegerField(unique=True)  # To prevent duplicates

    def __str__(self):
        return self.name

