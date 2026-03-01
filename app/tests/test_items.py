import pytest
from django.urls import reverse
from app.models import Item


@pytest.mark.django_db
def test_create_item(client):
    response = client.post(reverse('item_create'), data={
        'name': 'Test Item',
        'description': 'A test item.'
    }, content_type='application/json')
    assert response.status_code == 201
    assert Item.objects.filter(name='Test Item').exists()


@pytest.mark.django_db
def test_list_items(client):
    Item.objects.create(name='Item1', description='Desc1')
    response = client.get(reverse('item_list'))
    assert response.status_code == 200
    assert len(response.json()) >= 1


@pytest.mark.django_db
def test_update_item(client):
    item = Item.objects.create(name='Old', description='Old desc')
    response = client.put(
        reverse('item_update', args=[item.id]),
        data={"name": "New", "description": "New desc"},
        content_type='application/json'
    )
    assert response.status_code == 200
    item.refresh_from_db()
    assert item.name == 'New'


@pytest.mark.django_db
def test_delete_item(client):
    item = Item.objects.create(name='ToDelete', description='')
    response = client.delete(reverse('item_delete', args=[item.id]))
    assert response.status_code == 200
    item_exists = Item.objects.filter(id=item.id).exists()
    assert not item_exists
