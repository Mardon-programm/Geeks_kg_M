from django.db import models

# Create your models here.

class AcademyInfo(models.Model):
    name = models.CharField(max_length=155)
    adress = models.TextField()
    prhone_num = models.CharField(max_length=15)
    email = models.EmailField()
    about = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    

class Cours(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=155)

    def __str__(self):
        return self.title
    
class ContactForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"

