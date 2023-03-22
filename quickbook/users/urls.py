from django.urls import path
from . import views


app_name = 'users'


urlpatterns = [
    path('register', views.SignUp.as_view(), name="register"),
    path('user_panel', views.UserPanel.as_view(), name="user_panel"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('employees', views.EmployeesList.as_view(), name='employees_list'),
    path('delete/<int:pk>', views.EmployeeDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.EmployeeUpdate.as_view(), name='update'),
]
