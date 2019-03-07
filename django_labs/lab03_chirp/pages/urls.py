from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('pages/add_post', views.AddPostCreateView.as_view(), name='add_post'),
    # path('pages/<int:pk>/my_chirps/', views.MyChirpsView.as_view(), name='my_chirps')
    path('pages/<int:pk>/edit/', views.ChirpUpdateView.as_view(), name='edit_post'),
    path('pages/<int:pk>/delete', views.ChirpDeleteView.as_view(), name='post_delete'),


]

