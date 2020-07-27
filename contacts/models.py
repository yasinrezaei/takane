from django.db import models
from datetime import datetime
class Contacts(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    message=models.TextField()
    contact_date=models.DateTimeField(default=datetime.now,blank=True,null=True)
    user_id=models.IntegerField()
    takane=models.TextField()
    field=models.CharField(max_length=100)
    ability=models.TextField()
    takane_now=models.TextField()
    def __str__(self):
        return self.name
