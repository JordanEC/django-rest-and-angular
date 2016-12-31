from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.renderers import HTMLFormRenderer
from sample_1 import views
from .api import *
"""
urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^authors/$', AuthorApi.as_view()),
    #url(r'^authors/$', views.AuthorList.as_view()),
    #url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view()),
    url(r'^books/$', BookApi.as_view()),
    #url(r'^books/$', views.BookList.as_view()),
    #url(r'^books/(?P<pk>[0-9]+)/$', views.BookList.as_view()),
    #url(r'^users/$', views.UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^home', TemplateView.as_view(template_name='sample_1/home.html'), name='home'),
]
"""
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = router.urls
