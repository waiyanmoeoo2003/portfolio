from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from account.decorators import my_decorator
from portfolio.api.serializers import PortfolioSerializer, PortfolioCreateSerializer, ActivateDeactivateSerializer
from portfolio.models import Portfolio

from rest_framework.pagination import PageNumberPagination



class PortfolioViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Portfolio.objects.all()
    def get_serializer_class(self):
        if self.action in ("create"):
            return PortfolioCreateSerializer
        elif self.action == "status_toggle":
            return ActivateDeactivateSerializer
        return PortfolioSerializer

    def get_permissions(self):
        if self.action in ("get_active", "list", "retrieve"):
            permission_classes = [AllowAny]
        else:
            permission_classes = self.permission_classes

        return [permission() for permission in permission_classes]

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

    def update(self, request, *args, **kwargs):
        print(bool(IsAuthenticated))
        print("UpdateWork")
        response = super().update(request, *args, **kwargs)

        instance = self.get_object()
        return response

    @action(detail = False, methods = ["get"], permission_classes=[AllowAny])
    def get_active(self, request):

        active_portfolio = Portfolio.objects.get_active_one()
        serializer = PortfolioSerializer(active_portfolio)
        return Response(serializer.data)

