from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourite, name='favourite'),
    path('add_to_favourite/<product_id>', views.add_to_favourite, name='add_to_favourite'),
    path('remove_from_favourite/<product_id>', views.remove_from_favourite, name='remove_from_favourite'),
] 