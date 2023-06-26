from typing import Any, Dict
from django.shortcuts import render
from .models import ItemModel, MEAL_TYPES
from django.views import generic

# Create your views here.
class MenuList(generic.ListView):
    queryset = ItemModel.objects.order_by("meal")
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPES
        return context

class MenuItemDetailView(generic.DetailView):
    model = ItemModel
    template_name = "restaurant_menu/menu_item_detail.html"