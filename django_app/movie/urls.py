from django.conf.urls import url

from movie import views

app_name='movie'

urlpatterns = [
    url(r'^statistics/', views.statistics),
    url(r'^search/', views.search, name='api_search'),
    url(r'^app_test/', views.app_test)
]