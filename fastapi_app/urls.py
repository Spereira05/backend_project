from django.urls import path
from . import views

urlpatterns = [
    path('mangadex/', views.proxy_view, name='proxy_view'),
]