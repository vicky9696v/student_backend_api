from django.db import models


class Students(models.Model):
    name =  models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10,unique=True)
    physics = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    chemistry =models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)
    total_percentage = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name