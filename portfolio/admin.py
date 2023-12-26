from django.contrib import admin

from portfolio.forms import PortfolioForm
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    add_form = PortfolioForm
    model = Portfolio

    list_display = ("name", "professional", "available_status")

    fieldsets = (
        ("Portfolio", {"fields": ("name", "email")}),
        ("Information", {"fields": ("professional","phone_number", "address", "avator", "about")}),
        ("Portfolio Status", {"fields": ("available_status", "status")}),
    )

    