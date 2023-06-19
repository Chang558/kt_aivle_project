# temp/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from sign.models import User

User = get_user_model()

class Temp(models.Model):
    # 1. 게시글의 id 값
    id = models.AutoField(primary_key=True, null=False, blank=False)
    # 2. 제목
    title = models.CharField(max_length=100)
    # 3. 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 4. 작성자
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # user = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='temp_images/', null=True, blank=True)  # 이미지 업로드 필드 추가

    def __str__(self):
        return self.title