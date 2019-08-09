from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    path('writer_apply/', views.writer_apply, name='writer_apply'),
    path('writer_change/', views.writer_change, name='writer_change'),
    path('mypage/', views.mypage, name="mypage"),
    path('mypage_change/', views.mypage_change, name="mypage_change"),
]

# account app 내의 url 모음