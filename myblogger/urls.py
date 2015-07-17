"""myblogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.index'),
	url(r'^home/','blog.views.home'),
	url(r'blog/view/(?P<slug>[^\.]+).html','blog.views.view_post',name='view_blog_post'),	
    url('',include('social.apps.django_app.urls',namespace = 'social')),
    url('',include('django.contrib.auth.urls',namespace='auth')),
    url(r"/add_comment/(\d+)/$","blog.views.add_comment"),  
    url(r'^welcome/$','blog.views.welcome'),
    url(r"/register/(\d+)/$","blog.views.register"),
    url(r'/create/(\d+)$','blog.views.create'),
    url(r"/addblog/$","blog.views.addblog"),
    url(r'^ckeditor/',include('ckeditor.urls')),
]
 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)