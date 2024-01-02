from rest_framework import serializers
from portfolio.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = (
            "id",
            "name","email","phone_number","professional","address","avator",
            "available_status","linkedin","facebook","github"
        )

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
        print(self.validated_data.get('portfolio_id'))
        portfolio_exist =  bool(Portfolio.objects.get(pk=self.validated_data.get('portfolio_id')))

        if valid and portfolio_exist:
            return valid
        else:
            raise serializers.ValidationError({'status': ['ID does not exist.']})

        
        


