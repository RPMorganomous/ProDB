from django.conf.urls import url
from ProDB_app import views

urlpatterns = [
    url(r'^$',views.users,name='users'),

]