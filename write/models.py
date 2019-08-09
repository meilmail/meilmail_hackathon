from django.db import models
from django.utils import timezone
import sys
sys.path.append("..")
from account.models import Account


class Post(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now) # ('date published'): 작성날짜
    image = models.FileField(upload_to='files/%Y%M', blank = True)

    def __str__(self):
        return self.title
        #  ? 내가 만든 객채에 대해서 타이틀로 해주겠다.!!! 처음 객체를 생성한 뒤 그것에 붙여지는 이름은 Post이기 때문에 title을 제목으로 돌려주겠다 함.

    def summary(self):
        return self.body[ :100]
    

class Comment(models.Model):
    # 일대다 관걔 정해주는 방법(a와b는 종속적이다.)
    post=models.ForeignKey(Post, 
    on_delete=models.CASCADE)
    # 종속한모델이 없어졌을 때 종속된 것이 모두 사라짐
    content =models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)

   
    def __str__(self):
        
        return self.content
    
    # class Meta:
    #     # comment.objects.all().order_by('date_joined') 
