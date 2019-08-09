from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    # 장고 유저와 내가 만든 모델 1대1 연결
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    nickname = models.CharField(max_length=20)
    profile_image = models.ImageField(default="media/default_image.jpg")
    subscribe = models.ManyToManyField('self', blank = True)
    subscribed = models.ManyToManyField('self', blank = True)

    # 작가계정인지 일반계정인지 여부 false = 일반계정, true= 작가계정
    is_writer = models.CharField(default="일반", max_length=10)
    writer_name = models.CharField(max_length=20)
    introduction = models.TextField(max_length=200)
    hashtag = models.CharField(max_length=50)
    jenre = models.CharField(max_length=20)
    main_post1 = models.TextField(default="")
    main_post2 = models.TextField(default="")
    main_post3 = models.TextField(default="")

    def __str__(self):
        return self.user.username