from django.db import models

# Create your models here.

class Employee_info(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name
