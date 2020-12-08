from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('form',views.loginreg,name='loginreg'),
    path('signin',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('form/reset_password',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('form/reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('form/reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('form/reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]