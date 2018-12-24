from django.urls import path
from . import views

app_name = 'box'
urlpatterns = [
    path('', views.box_detail, name='box_detail'),
    path('add/<int:product_id>/', views.box_add, name='box_add'),
    path('remove/<int:product_id>/', views.box_remove, name='box_remove'),
]
