from django.urls import path
from blog import views

urlpatterns = [
    path('', views.Home.as_view(), name="index"),
    path('blog/<slug>/', views.BlogView.as_view(), name='detail'),
]
