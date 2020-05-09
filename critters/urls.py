from django.urls import path

from . import views

urlpatterns = [
    path('bugs/', views.bugs, name='bugs'),
    path('fishes/', views.fishes, name='fishes'),
    path('bug/<str:entity_id>', views.bug, name='bug'),
    path('fish/<str:entity_id>', views.fish, name='fish'),
    # path('loadfish', views.loadFish, name='loadFish'),
    # path('loadbug', views.loadBug, name='loadBug'),
]
