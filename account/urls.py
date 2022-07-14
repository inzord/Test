from django.conf.urls import url
from . import views

urlpatterns = [
    url('login/', views.user_login, name='login'),
    url('register/', views.register, name='register'),
    url('logout/', views.logout, name='logout'),
    url('home/', views.home, name='home'),
    url('account/', views.personal_account, name='account')
]
