from django.contrib import admin
from .models import Favourite, FavouritetItem

# Register your models here.
admin.site.register(Favourite)
admin.site.register(FavouriteItem)
