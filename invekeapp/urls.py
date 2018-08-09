from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^invest/', views.invest, name='invest'),
    url(r'^opportunity/', views.opportunity, name='opportunity'),
    url(r'^news/', views.news, name='news'),
    url(r'^aboutus/', views.aboutus, name='aboutus'),
    url(r'^contactus/', views.contactus, name='contactus'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^login/$', auth_views.login, {'template_name': 'register/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)