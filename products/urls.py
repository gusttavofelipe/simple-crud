from django.urls import path
from .views import ProductCreateView, HomeView, ProductDeleteView, ProductListView


app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', ProductCreateView.as_view(), name='register'),
    path('list/', ProductListView.as_view(), name='list'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
