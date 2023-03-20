from django.urls import path
from . import views


app_name = 'users'


urlpatterns = [
    path('register', views.SignUp.as_view(), name="register"),
    path('user_panel', views.UserPanel.as_view(), name="user_panel"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]
