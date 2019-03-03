from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import MakeShortUrl
from django.urls import reverse
import string
import random

template_name = 'lab02_url_shortner_app/index.html'
model = MakeShortUrl


def get_short_urls(request):
    short_urls = MakeShortUrl.objects.order_by("-id")
    context = {'short_urls': short_urls}
    return render(request, "lab02_url_shortner_app/index.html", context)


def add_url(request):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    short_code = ''.join(random.choice(chars)for _ in range(6))
    long_url = request.POST["long_url"]
    new_url = MakeShortUrl(short_code=short_code, long_url=long_url)
    new_url.save()
    return HttpResponseRedirect(reverse("lab02_url_shortner_app:get_short_urls"))


def go_here(request, short_code):
    item = get_object_or_404(MakeShortUrl, short_code=short_code)
    if item.number_of_clicks == "null":
        item.number_of_clicks = 1
    else:
        item.number_of_clicks += 1
    item.save()
    return HttpResponseRedirect(item.long_url)


    # new_item = GroceryItem(item_description=item_description, date_added=date_added)
    # new_item.save()
    # grocery_list = GroceryItem.objects.filter(was_purchased=False).order_by("-date_added")
    # # reverse looks at things in reverse to make the the url in this case it finds form frm urls.py
    # return HttpResponseRedirect(reverse("grocery_list_app:form"))

