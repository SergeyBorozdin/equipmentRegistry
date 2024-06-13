from django.db import models

class Equipment(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    dimension1 = models.FloatField()
    dimension2 = models.FloatField()
    dimension3 = models.FloatField()
    supplier_art = models.CharField(max_length=100)
    quantity = models.IntegerField()
    storage_location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='equipment_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def has_photo(self):
        return bool(self.photo and hasattr(self.photo, 'url'))
