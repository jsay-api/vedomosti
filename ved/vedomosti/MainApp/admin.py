from django.contrib import admin
from .models import *

class BeneficiaryModelAdmin(admin.ModelAdmin):
	list_display = ["ben_name", "ben_lastname"]
	list_display_links = ["ben_lastname"]
	class Meta:
		model = Beneficiary

class ABModelAdmin(admin.ModelAdmin):
	list_display = ["asset", "beneficiary"]
	class Meta:
		model = AssetsBeneficiaries

class BOModelAdmin(admin.ModelAdmin):
	list_display = ["beneficiary", "offshore"]
	class Meta:
		model = BeneficiariesOffshores


class OAModelAdmin(admin.ModelAdmin):
	list_display = ["offshore", "asset"]
	class Meta:
		model = OffshoresAssets


admin.site.register(Asset)
admin.site.register(Beneficiary, BeneficiaryModelAdmin)
admin.site.register(Offshore)
admin.site.register(AssetsBeneficiaries, ABModelAdmin)
admin.site.register(BeneficiariesOffshores, BOModelAdmin)
admin.site.register(OffshoresAssets, OAModelAdmin)