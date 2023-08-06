from django.db import models

# Create your models here.
class  compny2(models.Model):
    fullname=models.CharField(max_length=100)
    email=models .EmailField()
    age=models .IntegerField()
    barty=models .DateField()
    departhment= models.CharField(max_length=50,null=True)
    def __str__(self) :
      return self.fullname





class sall(models.Model):
    parcode=models.FloatField()
    namecode=models.CharField(max_length=100)
    sall=models.IntegerField ()
    def __str__(self) :
      return self.namecode






