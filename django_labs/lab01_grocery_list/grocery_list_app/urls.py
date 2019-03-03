from django.urls import path
from . import views

app_name = "grocery_list_app"


urlpatterns = [

        path('', views.get_items, name='form'),
        path('new_item', views.add_item, name='new_item'),
        path('remove_item/<int:pk>', views.remove_item, name='remove_item'),

]
