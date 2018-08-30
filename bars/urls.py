from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.bars_list),
    path('api/set/', views.bars_set),
]
