from django.db import models
from django.contrib.auth.models import User


class SearchEngine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=20)
    details = models.CharField(max_length=1000)
    search_date = models.DateField()

    def __str__(self):
        return str(self.keywords)
