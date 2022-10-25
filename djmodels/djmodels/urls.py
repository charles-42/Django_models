
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello, name="home"),
    path('hello/',views.hello),
    path('user/add/', views.user_create, name='user-create'),
    path('users/', views.user_list, name='user-list'), 
    path('users/<int:id>/', views.user_detail, name='user-detail'),
    path('session/', views.session, name='session'),
]
