from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('<int:pk>/', views.menuItemDetailView.as_view(), name='menu_item_detail'),
]