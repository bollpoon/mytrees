from django.urls import path

from . import views

urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('login/', views.login, name='login'),
    path('loginOK/', views.loginOK, name='loginOK'),
    path('circle/',views.circle, name = 'circle'),
    path('add/',views.add, name = 'add'),
    path('message/',views.message, name = 'message'),
    path('box/',views.box, name = 'box'),
    path('_self/',views._self, name = '_self'),
    path('friend/',views.friend, name = 'friend'),
    path('self_opinion/',views.self_opinion, name = 'self_opinion'),
    path('interest',views.interest,name = 'interest'),
    path('news',views.news,name = 'news'),
    path('add_2',views.add_2,name = 'add_2'),
]
