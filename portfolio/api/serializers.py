from rest_framework import serializers
from portfolio.models import Portfolio
from django.shortcuts import get_object_or_404

import os
from django.conf import settings
import time

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(PROJECT_ROOT)
STATIC_DIR = os.path.dirname(BASE)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = (
            "id",
            "name","email","phone_number","professional","address","avator",
            "available_status","linkedin","facebook","github"
        )

    def update(self, instance, validated_data):
        
        if not validated_data.get('avator'):
            validated_data['avator'] = instance.avator
            
        else:
            file_path  = os.path.join(STATIC_DIR,"media/" + instance.avator.name)

            if os.path.exists(file_path):
                os.remove(file_path)

            rand_number = int(time.time() * 1000)
            validated_data['avator'].name = f"{rand_number}.jpg"

        instance = super().update(instance, validated_data)

        return instance

class PortfolioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = (
            "name","email","phone_number","professional","address","avator",
            "available_status","linkedin","facebook","github"
        )

class ActivateDeactivateSerializer(serializers.Serializer):
    portfolio_id = serializers.IntegerField(label = "Portfolio ID")

    def is_valid(self, raise_exception=False):
        valid = super(ActivateDeactivateSerializer, self).is_valid(raise_exception=raise_exception)
        portfolio_exist =  bool(Portfolio.objects.filter(id=self.validated_data.get('portfolio_id')))

        if valid and portfolio_exist:
            return valid
        else:
            raise serializers.ValidationError({'status': ['ID does not exist.']})

        
        


