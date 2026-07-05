from django.db import models

# Create your models here.

class tasks(models.Model):

    tittle = models.CharField(max_length=50)
    detail = models.CharField(max_length=500,default="")
    status = models.CharField(max_length=50,default="not completed")

    def __str__(self):
        return self.tittle
    