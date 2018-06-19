from django.conf.urls import url
from articleapp import views

urlpatterns = [
    url(r'^article/$', views.article_api),

]
