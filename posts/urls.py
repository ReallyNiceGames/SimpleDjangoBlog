from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name="list"),
    path('create/', views.post_create, name="create"),
    path('<slug>/', views.post_display, name="display"),
] + debug_toolbar_urls()

