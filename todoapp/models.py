
import uuid
from django.db import models

# Create your models here.


class Todo(models.Model):
   
    name = models.CharField(max_length=255, null=True)
    task = models.CharField(max_length=2525,null=True)
    created_at = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
 