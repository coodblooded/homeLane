from email import header
from tkinter import TRUE
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework_api_key.permissions import HasAPIKey
from .utils import validate_payload
import requests
from homelane.settings import BASE_URL
from rest_framework_api_key.models import APIKey
# Create your views here.


class BudgetHomeView(APIView):
    permission_classes = [HasAPIKey]
    def post(self, request):
        try:
            validate_payload(request.data, [ "maxPrice" , "minPrice" ], 'budget')
        except Exception as e:
            return Response(
                            {"status": False, "message": str(e)},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
        maxPrice = request.data.get("maxPrice")
        minPrice = request.data.get("minPrice")
        
        # Call Data Service
        header = {"Content-Type": "application/json", "OriginUrl":"127.0.0.1"}
        url = BASE_URL + f'data/query?type=budget&max_p={maxPrice}&min_p={minPrice}'
        response = requests.get(url, headers=header)
        _data = []
        if response.status_code == 200:
            _data = response.json().get('result', [])
        return Response(
                        {"status": True, "result": _data},
                        status=status.HTTP_200_OK,
                    )


class HomeSqftView(APIView):
    permission_classes = [HasAPIKey]
    def post(self, request):
        try:
            validate_payload(request.data, [ "minSqft"], 'sqft')
        except Exception as e:
            return Response(
                            {"status": False, "message": str(e)},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
        minSqft = request.data.get("minSqft")
        
        # Call Data Service
        header = {"Content-Type": "application/json", "OriginUrl":"127.0.0.1"}
        url = BASE_URL + f'data/query?type=sqft&min_s={minSqft}'
        response = requests.get(url, headers=header)
        _data = []
        if response.status_code == 200:
            _data = response.json().get('result', [])
        return Response(
                        {"status": True, "result": _data},
                        status=status.HTTP_200_OK,
                    )


class HomeYearView(APIView):
    permission_classes = [HasAPIKey]
    def post(self, request):
        try:
            validate_payload(request.data, [ "year"], 'year')
        except Exception as e:
            return Response(
                            {"status": False, "message": str(e)},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
        year = request.data.get("year")
        
        # Call Data Service
        header = {"Content-Type": "application/json", "OriginUrl":"127.0.0.1"}
        url = BASE_URL + f'data/query?type=year&yr={year}'
        response = requests.get(url, headers=header)
        _data = []
        if response.status_code == 200:
            _data = response.json().get('result', [])
        return Response(
                        {"status": True, "result": _data},
                        status=status.HTTP_200_OK,
                    )



class GetNewApiKey(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        api_key, key = APIKey.objects.create_key(name="get-api-key")

        return Response({"status": True, "API-KEY": key},
                        status=status.HTTP_200_OK,)
                    