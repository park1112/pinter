from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    ## 35강 ,아티클 모델설정
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    #project = models.ForeignKey(project, on_delete=models.SET_NULL, related_name='article', null=True)


    title = models.CharField(max_length=200, null=True)     ## 제목 !
    image = models.ImageField(upload_to='article/', null=False)     ## 이미지
    content = models.TextField(null=True)       ## 내용 !!

    created_at = models.DateField(auto_now_add=True, null=True)     ## 언제 만들어 졌는지 확인가능 (생성된 시간 저장됨)

