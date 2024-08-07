from http import HTTPStatus
from products.models import Product
from django.urls import reverse
from django.contrib.messages import get_messages
import pytest


class TestViews():
    def test_home_view_sould_return_ok(self, client):
        response = client.get('http://127.0.0.1:8000/')
        assert response.status_code == HTTPStatus.OK 
    
    @pytest.mark.django_db
    def test_product_list_view_sould_return_ok(self, client):
        response = client.get('http://127.0.0.1:8000/list/')
        assert response.status_code == HTTPStatus.OK 
    
    @pytest.mark.django_db
    def test_product_create_view_should_create_and_redirect(self, client):
        data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'value': 100.0,
            'available': True
        }

        response = client.post(reverse('products:register'), data)
        storage = get_messages(response.wsgi_request)
        messages = [msg.message for msg in storage]

        assert Product.objects.filter(name='Test Product').exists()
        assert response.status_code == HTTPStatus.FOUND
        assert response.url == reverse('products:list')
        assert 'Product registered successfully!' in messages
