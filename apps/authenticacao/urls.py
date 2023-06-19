from django.urls import path
from . import views


urlpatterns = [
    #/auth/register
    path('register/', views.register, name='register'),
    #/auth/active_account/uidb4
    path('active_account/<uidb4>/<token>', views.active_account, name='active_account'),
    #/auth/login
    path('login/', views.login, name='login'),
    #/auth/logout
    path('logout/', views.logout, name='logout'),
]