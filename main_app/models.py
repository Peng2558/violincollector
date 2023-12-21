from django.db import models
from django.urls import reverse
# Create your models here.

class Violin(models.Model):
    name = models.CharField(max_length=100)
    provenance = models.CharField(max_length=100)
    year = models.IntegerField()
    inventory_no = models.IntegerField()
    tone = models.TextField(max_length=250)
    length = models.CharField(max_length=100)
    price =  models.CharField(max_length=100)

    def __str__(self):
     return self.name
    
    def get_absolute_url(self):
     return reverse('detail', kwargs={'violin_id': self.id})
    