from django.urls import path
from . import views

app_name = "lab02_url_shortner_app"

urlpatterns = [
    path('', views.get_short_urls, name='get_short_urls'),
    path('add_url', views.add_url, name='add_url'),
    path('go_here/<short_code>', views.go_here, name="go_here")
#     path(whatshowsup in the url, view connection, name for ridirect)



]
