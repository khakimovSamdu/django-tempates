from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Smartphone
import json
from tinydb import TinyDB
# Create your views here.

def homepage(request):
    data = ['Samsung', 'Apple', 'Nokia', 'Oppo', 'Vivo', 'Huawei', 'Redmi']
    phone = {"phone": data}
    return render(request, 'index.html', context=phone)

def brend_all(request, brend):
    data = Smartphone.objects.filter(name__contains = brend, company__contains = brend)
    ruyxat = []
    for item in data:
        ruyxat.append(item.to_dict())
    return render(request, 'muzey.html', context={'phones':ruyxat})

def add(request: HttpRequest):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        data = json.loads(data)
        create = Smartphone.objects.create(
            name = data['name'],
            company = data['company'],
            color = data['color'],
            RAM = data['RAM'],
            memory = data['memory'],
            price = data['price'], 
            img_url = data['img_url'], 
        )
        return JsonResponse({"statust":"ok"})
    else:
        return JsonResponse({"method": "error"})
