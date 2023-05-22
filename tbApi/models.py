from django.db import models

# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    location = models.CharField(max_length=60)
    sellerUser = models.ForeignKey
    photos = models.ImageField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title
