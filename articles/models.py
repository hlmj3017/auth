from django.db import models
from accounts.models import User # 방법1
from django.conf import settings # 방법2
from django.contrib.auth import get_user_model # 방법3
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set = 장고가 자동으로 추가해주는 칼럼 -> article이 comment에 접근
    
    # # 유저모델을 참조하는 경우
    # # 방법 1. (권장하지 않음)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # 변경가능성이 있는 데이터는 변수화해서 사용하는 것이 좋음
    
    # # 방법 2. (권장) settings.AUTH_USER_MODEL == 'accounts.User'
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # settings에 있는 accounts.User를 가져와서 사용

    # 방법 3. (권장)
    # user: 게시물을 참조하는 사람
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # 첫번째 User를 가져옴 
    # user_id = 

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 1 : N 관계 설정 / 내용과 article 객체가 들어감
    # article_id = 장고가 자동으로 추가해주는 칼럼

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id =       -> user와 comment 1 : N 연결