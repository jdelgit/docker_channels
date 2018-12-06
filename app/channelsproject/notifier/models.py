from django.db import models

# Create your models here.
class DummyModel(models.Model):
    data = models.CharField(max_length=255, null=True, blank=True, default=10)