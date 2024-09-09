from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
