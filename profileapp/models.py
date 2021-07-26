from django.db import models

# Create your models here.


class Profile(models,Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
                # OneToOneField (다대다, 하나의 유저에 하나의 프로필만 가능)
                # on_delete=models.CASCADE, ** 유저가 삭제되면 데이터도 같이 삭제된다 **
                # related_name='profile'    ** requset.user.profile.nickname 으로 바로 받아올수 있다 따로 변수 만들지 않고
    image = models.ImageField(upload_to='profile/', null=True)
                # (upload_to='profile/'     ** 업로드 할 위치를 정한다 **
                # null=True     ** 꼭 이미지를 업로드 하지 않아도 된다 **
    nickname = models.CharField(max_length=20, unique=True, null=True)     # unique=True  1개만 가질수 있다 유일하다
    message = models.CharField(max_length=100, null=True)