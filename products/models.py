from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=100)


class Brand(models.Model):
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    is_in_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.title_en


class Category(models.Model):
    title_fa = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    is_in_slider = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.parent.title_fa + ' > ' if self.parent else ''}{self.title_fa}"


# Create your models here.
class Product(models.Model):
    title_fa = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2)
    price_without_discount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    is_active = models.BooleanField(default=True)
    is_in_slider = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    color = models.CharField(max_length=255)

    added_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title_fa}"
