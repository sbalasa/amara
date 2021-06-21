from django.db import models

subscription_choices = (
    ('FREE', 'FREE'),
    ('PAID', "PAID"),
    ('PRO', "PRO")
)
class Subscriptions(models.Model):
    class Meta:
        verbose_name_plural = "Subscriptions"

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    subscription = models.CharField(max_length=20, choices=subscription_choices)

    def __str__(self):
        return self.name
