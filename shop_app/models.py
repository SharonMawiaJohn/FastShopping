from django.db import models

# Create your models here.
class Product(models,Model):
    CATEGORY = (("Electronics", "ELECTRONICS"),
                ("Groceries", "GROCERIES"),
                ("Clothings", "CLOTHINGS")
                )
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank = True, null = True)
    image = models.ImageField(upload_to="img")
    description = models.TextField(max_digit=10,decimal_places=2)
    category = models.CharField(max_length=15,choices=CATEGORY, blank=True, null=True)

    def __str__(self):
        return self.name