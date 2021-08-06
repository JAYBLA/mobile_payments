from django.urls import path 
from django.contrib.auth import views as auth_views

from .import views

app_name = 'account'

urlpatterns = [
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:id>/edit/', views.profile_update, name='profile_update'),
    
    #Admin
    path('admin-login/', views.UserLoginView.as_view(), name='admin_login'),

    path('admin_logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'),name='admin_logout',),
]