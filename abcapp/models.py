from django.db import models

# Create your models here.
class ABC(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    salary= models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self):   # to display the  frstand lastnames and phnno. in admin page
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)
