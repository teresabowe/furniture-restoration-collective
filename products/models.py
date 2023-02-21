from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
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


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    crafter = models.ForeignKey('Crafter', null=True, blank=True, on_delete=models.SET_NULL)
    source = models.ForeignKey('Source', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
