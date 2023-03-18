from django.urls import path
from . import views

app_name = 'users'  # To biedzie przestrzeń nazw w aplikacji main do uniknięcia niejednoznaczności

urlpatterns = [
    path('register', views.SignUp.as_view(), name="register"),
    path('user_panel', views.UserPanel.as_view(), name="user_panel"),
]

