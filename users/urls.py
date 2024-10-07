from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

] + debug_toolbar_urls()