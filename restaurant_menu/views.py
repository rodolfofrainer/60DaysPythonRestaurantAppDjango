from typing import Any, Dict
from django.shortcuts import render
from .models import ItemModel
from django.views import generic

# Create your views here.
class MenuList(generic.ListView):
    queryset = ItemModel.objects.order_by("meal")
    template_name = "index.html"
    
    def get_context_data(self):
        context = {"meals":"Pizza"}
        return context

class menuItemDetailView(generic.DetailView):
    model = ItemModel
    template_name = "menu_item_detail.html"