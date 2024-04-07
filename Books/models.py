from django.db import models


class books(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title

# Create your models here.
