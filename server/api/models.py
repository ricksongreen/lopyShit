from django.db import models

class Toilet(models.Model):
    place = models.CharField(max_length=50)
    toiletPaper = models.FloatField()
    maxAmountOfToiletRolls = models.IntegerField(default = 3)
    toiletRollSize = models.FloatField()
    extraDistance = models.FloatField()

class Usage(models.Model):
    usageDateTime = models.DateTimeField(auto_now_add=True, blank=True)
    toilet = models.ForeignKey(Toilet, on_delete=models.CASCADE)

class Tag(models.Model):
    uid = models.CharField(max_length=128, primary_key=True)

class Refiller(models.Model):
    name = models.CharField(max_length=50)
    tag = models.OneToOneField(Tag, on_delete=models.CASCADE)

class Refill(models.Model):
    refillDateTime = models.DateTimeField(auto_now_add=True, blank=True)
    refiller = models.ForeignKey(Refiller, on_delete=models.CASCADE)
    toilet = models.ForeignKey(Toilet, on_delete=models.CASCADE)
