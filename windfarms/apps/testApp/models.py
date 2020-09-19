from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name
# t = Topping.objects.create(name="anchovies", price=3.50)


class Windfarm(models.Model):
    name = models.CharField(max_length=64)
    location = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class WindmillPowerPlant(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    engine = models.TextField()
    output = models.IntegerField()
    parentFarm = models.ForeignKey("Windfarm", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=20)
    hash = models.CharField(max_length=20)

    def __str__(self):
        return self.username
