"""webapps URL Configuration

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
from rjb import views as rjb_views
from rjb import login as rjb_login
from rjb import upload as rjb_upload
from rjb import show as rjb_show
from rjb import getPic as rjb_getPic
from rjb import register as rjb_register
from rjb import tagit as rjb_tag
from rjb import userinfo as rjb_info
from rjb import history as rjb_history
from Test import views as Test_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', rjb_login.login),
    url(r'^do_login/', rjb_login.do_login),
    url(r'^do_logout/', rjb_login.do_logout),
    url(r'^upload/', rjb_upload.upload),
    url(r'^uploadImg/', rjb_upload.uploadImg),
    url(r'^showImg/', rjb_show.showImg),
    url(r'^getPic/', rjb_getPic.getPic),
    url(r'^register/', rjb_register.register),
    url(r'^do_register/', rjb_register.do_register),
    url(r'^tagit/', rjb_tag.tag_it),
    url(r'^tag/', rjb_tag.tag),
    url(r'^info/', rjb_info.info),
    url(r'^modify/', rjb_info.modify),
    url(r'^do_modify/', rjb_info.do_modify),
    url(r'^tags_by_id/', rjb_tag.tags_by_id),
    url(r'^test/', Test_views.test),
    url(r'^history/', rjb_history.history),
    url(r'^getpicbyid/', rjb_getPic.getpicbyid),
    url(r'^do_uploadface/', rjb_info.upload_face),
    url(r'^del_tags/', rjb_tag.del_tags),
    url(r'^search_by_tag/', rjb_tag.search_by_tag),
    url(r'^get_result/', rjb_tag.get_result),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
