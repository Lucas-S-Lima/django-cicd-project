
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Item
from django.views.decorators.csrf import csrf_exempt
import json

def item_list(request):
	items = Item.objects.all().values()
	return JsonResponse(list(items), safe=False)

def item_detail(request, pk):
	item = get_object_or_404(Item, pk=pk)
	return JsonResponse({
		'id': item.id,
		'name': item.name,
		'description': item.description,
		'created_at': item.created_at,
		'updated_at': item.updated_at,
	})


@csrf_exempt
def item_create(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		item = Item.objects.create(
			name=data.get('name', ''),
			description=data.get('description', '')
		)
		return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description}, status=201)
	return JsonResponse({'error': 'POST required'}, status=400)


@csrf_exempt
def item_update(request, pk):
	item = get_object_or_404(Item, pk=pk)
	if request.method == 'PUT':
		data = json.loads(request.body)
		item.name = data.get('name', item.name)
		item.description = data.get('description', item.description)
		item.save()
		return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description})
	return JsonResponse({'error': 'PUT required'}, status=400)


@csrf_exempt
def item_delete(request, pk):
	item = get_object_or_404(Item, pk=pk)
	if request.method == 'DELETE':
		item.delete()
		return JsonResponse({'deleted': True})
	return JsonResponse({'error': 'DELETE required'}, status=400)
