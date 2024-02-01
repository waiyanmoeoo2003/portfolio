from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from portfolio.api.views import PortfolioViewSet


router = DefaultRouter()
router.register("", PortfolioViewSet, basename = "portfolio")

urlpatterns = [
    path("", include(router.urls)),
]