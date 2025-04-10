from django.db import models
from django.urls import reverse

class Experiment(models.Model):
    """
    A simple model to track silicon photonics experiments
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    wavelength = models.FloatField(help_text="Wavelength in nm")
    power = models.FloatField(help_text="Power in mW")
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('experiment-detail', args=[str(self.id)])