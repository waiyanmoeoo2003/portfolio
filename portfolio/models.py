from django.db import models
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField, PPOIField

class CustomPortfolioManager(models.Manager):
    def get_active_one(self):
        return self.get_queryset().filter(status=True).first()

class Portfolio(models.Model):
    name = models.CharField(max_length = 30, blank = True, null = False, verbose_name = _("Portfolio Name"))
    email = models.EmailField(blank = True, verbose_name = _("Portfolio Email"))
    phone_number = models.CharField(max_length = 30, blank = True, verbose_name = _("Portfolio Phone Number"))
    professional = models.CharField(max_length = 50, blank = True, verbose_name = _("Professional"))
    address = models.CharField(max_length = 255, blank = True , verbose_name = _("Portfolio Address"))
    avator = VersatileImageField(
        upload_to="portfolio/" , 
        null=True , 
        blank=True ,
        ppoi_field="ppoi", 
        verbose_name = _("Portfolio Avator"))
    ppoi = PPOIField(null=True, blank=True)
    about = models.TextField(verbose_name = _("Portfolio About"))
    available_status = models.BooleanField(default = 1, verbose_name = _("Portfolio Available"))
    linkedin = models.URLField(verbose_name = _("Linkedin"), blank = True, unique = True)
    facebook = models.URLField(verbose_name = _("Facebook Link"), blank = True, unique = True)
    github = models.URLField(verbose_name = _("Github Link"), blank = True, unique = True)
    status = models.BooleanField(default = 0 , verbose_name = _("Portfolio Status"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Time"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated Time"))

    objects = CustomPortfolioManager()
    @classmethod
    def check_status(self):
        is_portfolio_active = bool(self.objects.filter(status = True))
        return is_portfolio_active
    
    def change_status(self):
        self.status = not bool(self.status)
        print(self.status)
        self.save()

    def __str__(self):
        return self.name

class Experiance(models.Model):
    portfolio = models.ForeignKey(Portfolio, verbose_name=_("Portfolio Name"), on_delete=models.CASCADE)
    company = models.CharField(_(""), max_length=50)
