from django.db import models


class Brand(models.Model):
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    is_in_slider = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.parent.name + ' > ' if self.parent else ''}{self.name}"


# Create your models here.
class Product(models.Model):
    title_fa = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2)
    price_without_discount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    is_active = models.BooleanField(default=True)
    is_in_slider = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)

    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title_fa}"
