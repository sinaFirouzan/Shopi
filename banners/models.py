from django.db import models


# Create your models here.
class Banner(models.Model):
    path = models.URLField(max_length=200)
    image = models.ImageField(upload_to='banners')
    is_active = models.BooleanField(default=True)
