from django.db import models

# Create your models here.
class Demo(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)

    phone=models.IntegerField(default=0)

    def __str__(self):   # to display the  frstand lastnames and phnno. in admin page
        return self.first_name
