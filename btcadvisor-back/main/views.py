from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import status, response, views

def main_page(request):
    user = request.user
    return render(request,'main/dashboard.html',{})
