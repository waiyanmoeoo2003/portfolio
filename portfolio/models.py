from django.db import models
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField


# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length = 30, blank = True, null = False, verbose_name = _("Portfolio Name"))
    email = models.EmailField(blank = True, verbose_name = _("Portfolio Email"))
    phone_number = models.CharField(max_length = 30, blank = True, verbose_name = _("Portfolio Phone Number"))
    professional = models.CharField(max_length = 50, blank = True, verbose_name = _("Professional"))
    address = models.CharField(max_length = 255, blank = True , verbose_name = _("Portfolio Address"))
    avator = VersatileImageField(
        upload_to="portfolio/", 
        null=True, 
        blank=True,
        verbose_name = _("Portfolio Avator")
    )
    about = models.TextField(verbose_name = _("Portfolio About"))
    available_status = models.BooleanField(default = 1, verbose_name = _("Portfolio Available"))
    status = models.BooleanField(default = 0 , verbose_name = _("Portfolio Status"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Time"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated Time"))