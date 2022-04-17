from rest_framework import serializers
from data_service.models import HouseData

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseData
        fields = '__all__'