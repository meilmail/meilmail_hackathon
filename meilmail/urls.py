"""meilmail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import main.views
import write.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    path('<int:writer_id>/writer_info',main.views.writer_info, name='writer_info'),
    path('subscribe/<int:writer_id>', main.views.subscribe, name='subscribe'),
    path('unsubscribe/<int:writer_id>', main.views.unsubscribe, name='unsubscribe'),
    path('<int:post_id>/detail', write.views.detail, name='detail'),
    path('write/', write.views.write, name="write"),
    path('<int:post_id>/delete',write.views.delete, name='delete'),
    path('<int:post_id>/edit',write.views.edit, name='edit'),
    path('<int:post_id>/comment', write.views.comment_create, name='comment'),
    path('account/', include('account.urls')),
]

# 개발 환경에서 Image 사용 가능하게 해주는 코드

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)