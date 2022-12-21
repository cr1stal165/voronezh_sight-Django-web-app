from django.db import models


class Architect(models.Model):
    name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    year_of_death = models.IntegerField()


class Address(models.Model):
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=10)


class Sight(models.Model):
    sight_name = models.CharField(max_length=500)
    building_date = models.IntegerField()
    image = models.ImageField(upload_to='sight_image')
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Excursion(models.Model):
    excursion_name = models.CharField(max_length=100)
    excursion_time = models.IntegerField()
    phone = models.CharField(max_length=15)
    price = models.IntegerField()


class History(models.Model):
    history = models.CharField(max_length=20000)
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE, blank=True, null=True)
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, blank=True, null=True)

