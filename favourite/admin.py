from django.contrib import admin
from .models import Favourite, FavouriteItem

# Register your models here.
admin.site.register(Favourite)
admin.site.register(FavouriteItem)
