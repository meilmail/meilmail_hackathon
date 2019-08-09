from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import Account

# Email을 위한 세팅
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=email, password=password)
        
        # 로그인에 실패한 경우
        if user is None:
            messages.info(request, ": 회원정보가 일치하지 않습니다. 다시 시도해주세요")
            return redirect('login')

        auth.login(request, user)
        return redirect("home")
    else:
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect("home")

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        nickname = request.POST.get('nickname')
        
        # 입력 값이 비어있을 때
        if nickname == "" or email == "" or password == "":
            messages.info(request,"회원가입 정보를 모두 기입해주세요.")
            return redirect('signup')

        # 비밀번호가 다를 때
        if not password == password_confirm:
            messages.info(request, ": 비밀번호가 다릅니다.")
            return redirect('signup')
        
        # Validation 성공한 경우
        user = User.objects.create_user(username=email, password=password)
        user.is_active = False # 인증 전까지 활성화 제어
        user.save()
        account = Account(user=user, email=email, nickname=nickname)
        account.save() # 일단 계정은 저장
        current_site = get_current_site(request)
        message = render_to_string('account/user_activate_email.html',{
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail_subject = "[매일메일] 회원가입 인증 메일입니다."
        user_email = user.username
        check_email = EmailMessage(mail_subject, message, from_email = settings.DEFAULT_FROM_EMAIL, to=[user_email])
        check_email.send()
        return render(request, 'account/signup_complete.html')
    else:
        return render(request, 'account/signup.html')

def activate(request, uid64, token):
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)
    
    if user is not None and account_activation_token.check_token(user, token):
        account = Account.objects.get(user=user)
        user.is_active = True
        user.save()
        account.is_writer = "일반"
        account.save()
        auth.login(request, user)
        return redirect('home')
    else:
        return HttpResponse('비정상적인 접근입니다.')
    

    
def writer_apply(request):
    if request.method == 'POST':
        writer_name = request.POST.get('writer_name')
        profile_image = request.FILES.get('profile_image', None)
        introduction = request.POST.get('introduction')
        hash_tag = request.POST.get('hash_tag')
        main_post1 = request.POST.get('main_post1')
        main_post2 = request.POST.get('main_post2')
        main_post3 = request.POST.get('main_post3')
        jenre = request.POST.get('jenre')

        try:
            account = Account.objects.get(user=request.user)
        except:
            print("no user")

    # 입력 값이 비어있을 때
        if writer_name == "" or introduction == "" or main_post1 == "" or jenre=="" or main_post2 == "" or main_post3 == "":
            messages.info(request,"작가 정보를 모두 기입해주세요.")
            return redirect('writer_apply')
        
        account.writer_name = writer_name
        account.introduction = introduction
        account.main_post1 = main_post1
        account.main_post2 = main_post2
        account.main_post3 = main_post3
        account.jenre = jenre
        account.hashtag = hash_tag
        if profile_image:
           account.profile_image = profile_image

        account.is_writer = "대기"
        account.save()
        return redirect("home") 
    else:
        if request.user.is_authenticated:
            context = {}
            account = Account.objects.get(user=request.user)
            context.setdefault('nickname', account.nickname)
            context.setdefault('thumbnail', account.profile_image)
            context.setdefault('is_writer', account.is_writer)

        return render(request,'account/writer_apply.html', context)

def writer_change(request):
    account = Account.objects.get(user=request.user)
    if request.method=="POST":
        writer_name = request.POST.get('writer_name')
        profile_image = request.FILES.get('profile_image', None)
        introduction = request.POST.get('introduction')
        hash_tag = request.POST.get('hash_tag')
        main_post1 = request.POST.get('main_post1')
        main_post2 = request.POST.get('main_post2')
        main_post3 = request.POST.get('main_post3')
        jenre = request.POST.get('jenre')
        try:
            account = Account.objects.get(user=request.user)
        except:
            print("no user")

    # 입력 값이 비어있을 때
        if writer_name == "" or introduction == "" or main_post1 == "" or jenre=="" or main_post2 == "" or main_post3 == "":
            messages.info(request,"작가 정보를 모두 기입해주세요.")
            return redirect('writer_apply')
        
        account.writer_name = writer_name
        account.introduction = introduction
        account.main_post1 = main_post1
        account.main_post2 = main_post2
        account.main_post3 = main_post3
        account.jenre = jenre
        account.hashtag = hash_tag
        if profile_image:
           account.profile_image = profile_image
        account.save()
        return redirect("home") 
    else:
        return render(request, 'account/writer_change.html', {'account' : account})

def mypage(request):
    context = {}
    account = Account.objects.get(user=request.user)
    context.setdefault('nickname', account.nickname)
    context.setdefault('thumbnail', account.profile_image)
    context.setdefault('is_writer', account.is_writer)

    context.setdefault('account', Account.objects.get(user=request.user))
  
    return render(request, 'account/mypage.html', context)

def mypage_change(request):
    account = Account.objects.get(user=request.user)
    if request.method=="POST":
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        profile_image = request.FILES.get('profile_image', '')

    # 입력 값이 비어있을 때
        if not password == password_confirm and not password and not password_confirm:
            messages.info(request, ": 비밀번호가 다릅니다.")
            return redirect('mypage_change')
        else:
            account.password = password

        if nickname:
            account.nickname = nickname
        
        if profile_image:
           account.profile_image = profile_image

        account.save()
        return redirect("home") 
    else:
        return render(request, 'account/mypage_change.html', {'account' : account})
