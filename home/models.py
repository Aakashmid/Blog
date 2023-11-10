from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=500)
    email=models.CharField( max_length=500)
    phone_no=models.IntegerField(default=0000000000)
    desc=models.TextField()
    # def init(self):
    #     return self.name
