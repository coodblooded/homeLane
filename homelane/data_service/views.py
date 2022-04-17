from django.shortcuts import render
from rest_framework.views import APIView 
from .permissions_bankend import BlocklistPermission
from rest_framework.response import Response
from rest_framework import status


from .models import HouseData
from django.db.models import Q
from .serializers import BudgetSerializer
# Create your views here.
class BudgetQueryView(APIView):
    permission_classes = [BlocklistPermission]

    def get(self,request):
        query_type = request.GET.get('type')
        if query_type == 'budget':
            max_price = int(request.GET.get('max_p'))
            min_price = int(request.GET.get('min_p'))
            objs = HouseData.objects.filter(Q(price__lte=max_price) & Q(price__gte=min_price)).all()

        if query_type == 'sqft':
            min_sqft = int(request.GET.get('min_s'))
            objs = HouseData.objects.filter(Q(sqft_living__gt=min_sqft)).all()


        if query_type == 'year':
            yr = int(request.GET.get('yr'))
            objs = HouseData.objects.filter(Q(yr_built__gt=yr) | Q(yr_renovated__gt=yr)).all()

        serializer = BudgetSerializer(objs, many=True)
        
        return Response(
                        {"status": True, "result": serializer.data},
                        status=status.HTTP_200_OK,
                    )
        