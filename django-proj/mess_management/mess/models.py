from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name
