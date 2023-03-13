import uuid

from django.db import models


class QuoteCategory(models.Model):

    class Meta:
        verbose_name_plural = "Quote Categories"

    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class QuoteCategoryDetail(models.Model):

    class Meta:
        verbose_name_plural = "Quote Category Detail"

    quotecategory = models.ForeignKey(QuoteCategory(), on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=00.00)

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price


PICKUP_CHOICES = (
    ("Y", "Yes, I need you to pickup my furniture"),
    ("N", "No, I will drop it to your shop"),
)


class Quote(models.Model):
    quote_number = models.CharField(max_length=32, null=False, editable=False)
    quotecategory = models.ForeignKey(QuoteCategory(), on_delete=models.SET_NULL, blank=True, null=True)
    quotecategorydetail = models.ForeignKey(QuoteCategoryDetail, on_delete=models.SET_NULL, blank=True, null=True)
    pickup = models.CharField(max_length=3, choices=PICKUP_CHOICES, default='N')
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    pickup_price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def _generate_quote_number(self):
        """
        Generate a random, unique quote number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.quote_number:
            self.quote_number = self._generate_quote_number()
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the pickup price.
        """
        if self.pickup == "Y":
            self.pickup_price = "50.00"
        super().save(*args, **kwargs)
