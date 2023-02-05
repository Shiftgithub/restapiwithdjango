from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
