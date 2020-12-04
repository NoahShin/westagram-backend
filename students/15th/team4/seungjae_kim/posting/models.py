from django.db import models
from user.models import Users

class Posts(models.Model):

    title = models.CharField(max_length = 100)
    User = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auo_now_add = True)
    image_url = models.URLField(max_length = 2000)

    class Meta:
        db_table = "Posts"

    
