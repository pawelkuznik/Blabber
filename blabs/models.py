from django.db import models

# Create your models here.


class Blab(models.Model):
    # id = models.Autofield(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

