from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    # Zmienia liczbe mnoga categoryes w panelu admina na Categories.
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # price = models.DecimalField(max_digits=9, decimal_places=2)
    #stock = models.DecimalField(6, 2, null=False)
    price = models.FloatField()
    stock = models.FloatField()
    image = models.TextField()

    def __str__(self):
        return self.title