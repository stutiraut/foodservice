"""mfscrm URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('accounts/login/',	auth_views.LoginView.as_view(),	name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),	name='logout'),

    #change password urls
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('accounts/password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',	auth_views.PasswordResetView.as_view(),	name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),	name='password_reset_done'),
    path('reset/<uidb64>/<token>/',	auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',	auth_views.PasswordResetCompleteView.as_view(),	name='password_reset_complete'),


]
