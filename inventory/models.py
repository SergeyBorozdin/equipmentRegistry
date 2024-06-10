from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    dimension1 = models.FloatField(default=0.0)  # значение по умолчанию
    dimension2 = models.FloatField(default=0.0)
    dimension3 = models.FloatField(default=0.0)
    supplier_art = models.CharField(max_length=200)
    quantity = models.IntegerField()
    storage_location = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='equipment_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
