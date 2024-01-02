from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import status


from portfolio.api.serializers import PortfolioSerializer, PortfolioCreateSerializer, ActivateDeactivateSerializer
from portfolio.models import Portfolio

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    
    def get_serializer_class(self):
        if self.action in ("create"):
            return PortfolioCreateSerializer
        elif self.action == "status_toggle":
            return ActivateDeactivateSerializer
        return PortfolioSerializer
    
    @action(detail = False, methods = ["post"])
    def status_toggle(self, request):
        serializer = ActivateDeactivateSerializer(data=request.data)
        if serializer.is_valid():
            instance = Portfolio.objects.get(pk=serializer.validated_data['portfolio_id'])
            if instance.status:
                instance.change_status()
                return Response({'message': 'Portfolio has been set to inactvie'},status=status.HTTP_200_OK)
            else:
                if Portfolio.check_status():
                    return Response({'message': 'Only One Portfolio is allowed to active'},status=status.HTTP_400_BAD_REQUEST)
                else:
                    instance.change_status()
                return Response({'message': 'Portfolio has been set to active'},status=status.HTTP_200_OK)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PortfolioStatusToggleViewSet(viewsets.ViewSet):

    @action(detail = False, methods = [])
    def change_status(self):
        return Response({'message': 'Custom action response'})
