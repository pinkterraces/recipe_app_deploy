from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    #username = models.OneToOneField(User, on_delete = models.CASCADE)
    user = models.CharField(max_length = 120)
    #password = models.CharField(max_length = 120)
    
    def __str__(self):
        return str(self.user)