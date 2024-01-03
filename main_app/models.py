from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

SERVICES = (
  ('B', 'Bridge Adjustment'),
  ('T', 'Tuning'),
  ('S', 'String Replacement'),
)

class Accessory(models.Model):
  name = models.CharField(max_length = 50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})






class Violin(models.Model):
    name = models.CharField(max_length=100)
    provenance = models.CharField(max_length=100)
    year = models.IntegerField()
    inventory_no = models.IntegerField()
    tone = models.TextField(max_length=250)
    length = models.CharField(max_length=100)
    price =  models.CharField(max_length=100)
    
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
     return f'{self.name} ({self.id})'
    

    def get_absolute_url(self):
     return reverse('detail', kwargs={'violin_id': self.id})
    
    def tuned_for_today(self):
     return self.tuneup_set.filter(date=date.today()).count() >= len(SERVICES)
    

class Tuneup(models.Model):
  date = models.DateField('Tune up Date')
  service = models.CharField(
    max_length=1,
    choices=SERVICES,
    default=SERVICES[0][0]
  )
  # Create a violin_id FK
  violin = models.ForeignKey(
    Violin,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_service_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
    