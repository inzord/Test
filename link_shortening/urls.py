from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_url),
    path('<slug:key>/', views.route_to_url, name='link-shortening-home'),
]
