from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    class Meta:
        db_table = 'Register'
        

