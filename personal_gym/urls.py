from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'login', login, name='login'),
    url(r'logout', logout_then_login, name='logout'),
    url(r'', include('academia.urls'))
]
