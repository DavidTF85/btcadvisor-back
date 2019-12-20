"""
homepage/views.py
"""
from rest_framework import status, response, views
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect



class VersionAPI(views.APIView):
    def get(self, request):
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'version f=': '= 0+1+1+2'
            }
        )
