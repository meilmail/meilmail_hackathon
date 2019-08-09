from django.shortcuts import render,redirect, HttpResponse
# Email을 위한 세팅
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
import datetime
import sys
sys.path.append("..")
from write.models import Post


def send_html_email(to, subject, template_name, context, sender=settings.DEFAULT_FROM_EMAIL):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, to = to)
    msg.content_subtype = "html"
    return msg.send()
    
def send_templates(request):
    send_html_email('ediblepotato@gmail.com', 'Hi', 'account/signup.html', {}) # account/template/account/파일.html 형태로 위치해야 함.
    return redirect('home')

def send_meilmail():
    #날짜 셋팅
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    date = nowDate.split('-')
    subject = '[매일메일]' + date[0] + '년 ' + date[1] + '월 ' + date[2] + '일 글 한 편 올립니다.'
    all_post = Post.objects.all()
    todaylist = []

    for post in all_post:
        todaylist.append(post)
        if str(post.pub_date) < str(now - datetime.timedelta(1)):
            break
    
    for post in todaylist:
        writer = post.account
        to = [writer.email for writer in writer.subscribed.all()]
        context = post.content
        today_mail = EmailMessage(subject=subject, body=context, from_email = settings.DEFAULT_FROM_EMAIL, to=to)
        today_mail.send()