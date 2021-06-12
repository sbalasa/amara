from django.db import models

class Subscriptions(models.Model):
    class Meta:
        verbose_name_plural = "Subscriptions"
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    subscriptions = models.CharField(max_length=20)

    def __str__(self):
        return self.name
