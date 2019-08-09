from django.shortcuts import render, redirect
from django.contrib import messages
import sys
sys.path.append("..")
from account.models import Account

# Create your views here.
def home(request):
  context = {}

  if request.user.is_authenticated:
    account = Account.objects.get(user=request.user)
    context.setdefault('nickname', account.nickname)
    context.setdefault('thumbnail', account.profile_image)
    context.setdefault('is_writer', account.is_writer)

  writer_list = Account.objects.filter(is_writer="작가")
  if writer_list:
    context.setdefault('writer_list', writer_list)

  return render(request, "main.html", context)

def writer_info(request, writer_id):
  context = {}

  if request.user.is_authenticated:
    account = Account.objects.get(user=request.user)
    context.setdefault('nickname', account.nickname)
    context.setdefault('thumbnail', account.profile_image)
    context.setdefault('is_writer', account.is_writer)
    context.setdefault('myAccount', Account.objects.get(user=request.user))

  context.setdefault('account', Account.objects.get(id=writer_id))
  
  return render(request, 'writer_info.html', context)
    
def subscribe(request, writer_id):
  if request.user.is_authenticated:
    myAccount = Account.objects.get(user=request.user)
    writerAccount = Account.objects.get(id=writer_id)

    if myAccount == writerAccount:
      messages.info(request, '본인을 구독할 수 없습니다.')
      redirect('writer_info', writer_id)

    myAccount.subscribe.add(writerAccount)
    writerAccount.subscribed.add(myAccount)

    writerAccount.save()
    myAccount.save()
    print(writerAccount.subscribed.all())
    print(myAccount.subscribe.all())
  else:
    return redirect("login")

  return redirect('writer_info', writer_id)

def unsubscribe(request, writer_id):
  if request.user.is_authenticated:
    myAccount = Account.objects.get(user=request.user)
    writerAccount = Account.objects.get(id=writer_id)

    myAccount.subscribe.remove(writerAccount)
    writerAccount.subscribed.remove(myAccount)

    writerAccount.save()
    myAccount.save()
  else:
    return redirect("login")

  return redirect("writer_info", writer_id)