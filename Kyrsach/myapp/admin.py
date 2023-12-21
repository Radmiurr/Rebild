from django.contrib import admin

from .models import Product, Reviews



admin.site.site_header = "IVT-222"
admin.site.site_title = "My shop"
admin.site.index_title = "My admin"


class Tovari(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    serch_fields = ("name",)
    list_editable = ("price", "description")
    actions = ('make_zero',)

    def make_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, Tovari)
admin.site.register(Reviews)
