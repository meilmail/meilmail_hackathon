from django.shortcuts import render, redirect
from .models import Post, Comment
from account.models import Account

# Create your views here.: 어떤 데이터가 어떻게 처리될 지 알려주는 함수! model과 templates를 연결.
def home(request):
    post_list = Post.objects.all() 
    return render(request, 'home.html', {'post_list':post_list})

    #쿼리셋과 메소드의 형식: "모델.쿼리셋(Object).메소드"
    #all():포스트로 만든 모든 쿼리셋 객체들을 불러오라는 소리
        #.count: 개수 반환
        # .first(): 첫번째 객체 반환
        # .last(): 마지막 객체 반환
    #쿼리셋:포스트 안에 있는 객체를 담아준다.모델로부터 객체의 목록을 전달받을 수 있음.=.object
    #쿼리셋을 이용해서 받은 데이터를 정렬, 표시하는 방법을 메소드라고 함.

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all().order_by('-pub_date')
    return render(request,"detail.html", {'post':post, 'comments': comments})

def write(request):
    if request.method=="POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('file', '')
        account = Account.objects.get(user=request.user)

        post = Post(account=account, title=title, content=content)

        if image:
            post.image = image
        
        post.save()
        return redirect('home')
    else:
        return render(request, 'write.html')

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    # 각 글의 고유한 아이디를()에 넣어야함, id=는 변수, post_id=상수값. 
    post.delete()
    return redirect('home')

#어려운 부분: 갱신하기
def edit(request,post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('')       

    else:
        post=Post.objects.get(id=post_id)
        return render (request, 'edit.html',{"post": post})

def comment_create(request, post_id):
    if request.method=="POST":
        post=Post.objects.get(id=post_id)
        comment=Comment(post=post)
        # 파랑포스트는 models에 있는 변수 post, 흰 포스트는 객체의 값 특정된 것(엄마=엄마이름)
        comment.content=request.POST['content']
        comment.save()
        
        return redirect('detail',post_id)

