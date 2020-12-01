from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phonenumber = models.CharField(max_length=13)
    email = models.EmailField(max_length=70)

    class Meta:
        db_table = 'users'

