
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('room_page/<int:pk>/', views.room, name="room"),
]
