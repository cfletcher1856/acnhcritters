from django.db import models


class Fish(models.Model):
    entity_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    image_64 = models.TextField()
    image_url = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    start_time = models.IntegerField(default=0, null=True)
    end_time = models.IntegerField(default=0, null=True)
    all_day = models.BooleanField(default=False)
    active_time = models.CharField(max_length=200)
    active_months = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "{0}".format(self.name)

class Bug(models.Model):
    entity_id = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    image_64 = models.TextField()
    image_url = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    start_time = models.IntegerField(default=0, null=True)
    end_time = models.IntegerField(default=0, null=True)
    all_day = models.BooleanField(default=False)
    active_time = models.CharField(max_length=200)
    active_months = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "{0}".format(self.name)
