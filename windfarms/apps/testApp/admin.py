from django.contrib import admin

from .models import Company, Windfarm, WindmillPowerPlant

admin.site.register(Company)
admin.site.register(Windfarm)
admin.site.register(WindmillPowerPlant)
