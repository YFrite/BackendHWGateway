import json

import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def get_and_post(request):
    if request.method == "GET":
        return requests.get(" http://192.168.0.105:8001/get_and_post")
    elif request.method == "POST":
        return requests.post("http://192.168.0.105:8001/get_and_post")

def redirected(request):
    return requests.get("http://192.168.0.105:8001/redirected")

def all_users(request):
    return requests.get("http://192.168.0.105:8001/users")

@csrf_exempt
def update_user(request, pk):
    return requests.post(f"http://192.168.0.105:8001/users/update/{pk}", json=request.body)

def delete_user(request, pk):
    return requests.get(f"http://192.168.0.105:8001/users/delete/{pk}")

@csrf_exempt
def add_user(request):
    return request.post("http://192.168.0.105:8001/users/add", json=request.body)

@csrf_exempt
def register(request):
    return requests.post(f"http://192.168.0.105:8001/register", json=request.body)

@csrf_exempt
def user_login(request):
    return requests.post(f"http://192.168.0.105:8001/login", json=request.body)