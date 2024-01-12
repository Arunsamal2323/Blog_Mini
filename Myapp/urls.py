from django.urls import path
from django.conf import settings

from Myapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path('blog/<>/', views.BlogDetails, name='BlogDetails'),
]
