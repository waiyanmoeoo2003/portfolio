from django import forms
from versatileimagefield.fields import SizedImageCenterpointClickDjangoAdminField

from .models import Portfolio

class PortfolioForm(forms.Form):
    class Meta:
        model = Portfolio
        fields = ("name","email","phone_number","professional","address","avator","ppoi","about","available_status","status",)

    