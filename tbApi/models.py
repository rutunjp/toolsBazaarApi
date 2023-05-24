from django.db import models
import uuid
# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()
    location = models.CharField(max_length=60)
    sellerUser = models.ForeignKey
    slug = models.SlugField(default=True, blank=True, null=True)
    photos = models.ImageField(null=True, blank=True)
    featured = models.BooleanField()
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True, unique=True)

    def __str__(self):
        return self.title


class ListingImage(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        upload_to="img", default="", null=True, blank=True)
