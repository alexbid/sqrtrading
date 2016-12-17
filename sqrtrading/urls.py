from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = [
               url(r'^stockscreener/', include('stockscreener.urls')),
               url(r'^admin/', admin.site.urls),
               url(r'^$', lambda r: HttpResponseRedirect('stockscreener/')),
#               url(r'^$', include('stockscreener.urls')),
#               url(r'^$', stockscreener.views.index, name='index'),
]
