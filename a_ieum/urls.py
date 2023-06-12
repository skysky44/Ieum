"""a_ieum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from posts import views
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('posts/', include('posts.urls')),
    path('balances/', include('balances.urls')),
    path('accounts/', include('accounts.urls')),
    path('my_messages/', include('my_messages.urls')),
    path('paints/', include('paints.urls')),
    path('chat/', include('chat.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path('browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
    #이메일 인증
    # path('',include('allauth.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
