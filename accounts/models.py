from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    # article_set =   -> 특정한 유저가 볼 수 있도록 저장한 set을 볼 수 있도록 
    # comment_set 