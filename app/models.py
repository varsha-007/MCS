from django.db import models

# Create your models here.


class ForwardPhysicalValues(models.Model):
    prod = models.CharField(max_length=250, null=True)
    mar = models.CharField(max_length=250, null=True)
    apr = models.CharField(max_length=250, null=True)
    may = models.CharField(max_length=250, null=True)
    q3 = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.prod}"


class SeaborneLastTradedLevels(models.Model):
    product = models.CharField(max_length=250, null=True)
    primary = models.CharField(max_length=250, null=True)
    secondary = models.CharField(max_length=250, null=True)

    def __str__(self) -> str:
        return f"{self.product}"
