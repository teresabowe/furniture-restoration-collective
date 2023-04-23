from django.db import models
from django.db.models import Q


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = "Sub Categories"

    name = models.CharField(max_length=254)
    category = models.ForeignKey(Category(), on_delete=models.CASCADE, default="1")
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Crafter(models.Model):
    first_name = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254, null=True, blank=True)
    specialisation = models.CharField(max_length=254, null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.first_name

    def get_friendly_name(self):
        return self.full_name


class Source(models.Model):
    source_name = models.CharField(max_length=254)
    source_friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.source_name

    def get_friendly_name(self):
        return self.source_friendly_name


ACTIVE = (
    ("Y", "Yes"),
    ("N", "No"),
)


class Review(models.Model):

    class Meta:
        verbose_name_plural = "Reviews"

    comment = models.CharField(max_length=500)
    crafter = models.ForeignKey(Crafter(), on_delete=models.CASCADE)
    active = models.CharField(max_length=3, choices=ACTIVE, default='N')

    def __str__(self):
        return self.comment


QUOTE = (
    ("Y", "Yes"),
    ("N", "No"),
)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    quote = models.CharField(max_length=3, choices=QUOTE, default='N')
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='', default="/noimage.png")
    crafter = models.ForeignKey('Crafter', null=True, blank=True, on_delete=models.SET_NULL)
    source = models.ForeignKey('Source', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
