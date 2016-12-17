from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
               url(r'^stockscreener/', include('stockscreener.urls')),
               url(r'^admin/', admin.site.urls),
               url(r'^$', views.index, name='index'),
]
