from django.db import models

class Toilet(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    toiletPaper = models.FloatField()

class Usage(models.Model):
    usageDateTime = models.DateTimeField()
    toilet = models.ForeignKey(Toilet, on_delete=models.CASCADE)

class Reviller(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=128)

class Revill(models.Model):
    revillDateTime = models.DateTimeField()
    reviller = models.ForeignKey(Reviller, on_delete=models.CASCADE)
    toilet = models.ForeignKey(Toilet, on_delete=models.CASCADE)
