from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import GroceryItem
from django.urls import reverse
from django.views import generic
from django.utils import timezone


template_name = 'grocery_list_app/form.html'
model = GroceryItem


def get_items(request):
    purchased_items = GroceryItem.objects.filter(was_purchased=True).order_by("-date_purchased")
    grocery_list = GroceryItem.objects.filter(was_purchased=False).order_by("-date_added")
    context = {
        'grocery_list': grocery_list,
        'purchased_items': purchased_items
    }
    return render(request, "grocery_list_app/form.html", context)


def add_item(request):
    item_description = request.POST["description"]
    date_added = timezone.now()
    new_item = GroceryItem(item_description=item_description, date_added=date_added)
    new_item.save()
    grocery_list = GroceryItem.objects.filter(was_purchased=False).order_by("-date_added")
    # reverse looks at things in reverse to make the the url in this case it finds form frm urls.py
    return HttpResponseRedirect(reverse("grocery_list_app:form"))


def remove_item(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.was_purchased = True
    item.date_purchased = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse("grocery_list_app:form"))




