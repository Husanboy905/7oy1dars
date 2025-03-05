from django.db import models
from django.contrib.auth.models import User


class Colors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    price = models.IntegerField()
    speed = models.IntegerField()
    year = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='main/index/', null=True, blank=True)


    def __str__(self):
        return self.name


class Comment(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.name}"










from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE)
    color = models.ForeignKey('Colors', on_delete=models.CASCADE)


from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.car}"
