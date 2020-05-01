from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icons/')
    body = models.CharField(max_length=5000)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.date()

    def summary(self):
        return self.body[:150]
