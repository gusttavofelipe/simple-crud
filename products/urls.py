from django.urls import path
from .views import ProductCreateView, HomeView, ProductListView


app_name = 'products'

urlpatterns = [
    path('register/', ProductCreateView.as_view(), name='register'),
    path('list/', ProductListView.as_view(), name='list'),
    path('', HomeView.as_view(), name='home'),
]
