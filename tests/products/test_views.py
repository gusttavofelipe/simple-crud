from http import HTTPStatus
from products.models import Product
from django.urls import reverse
from django.contrib.messages import get_messages
import pytest


class TestProductViews():
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

    @pytest.mark.django_db
    def test_product_delete_view_should_delete_and_redirect(self, client):
        product = Product.objects.create(
            name='Test Product', 
            description='Test Description',
            value=99.99, available=True
        )
        delete_url = reverse('products:delete', kwargs={'pk': product.pk})
        response = client.delete(delete_url)
        
        assert response.status_code == HTTPStatus.FOUND
        assert response.url == reverse('products:list')
        assert not Product.objects.filter(pk=product.pk).exists()
