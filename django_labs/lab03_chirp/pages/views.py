from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page


class HomePageView(ListView):
    model = Page
    template_name = 'home.html'

    def get_queryset(self):
        return Page.objects.order_by('-date_updated')


class AddPostCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'home.html'
    fields = ['body']
    login_url = 'login'
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        form.instance.username = self.request.user
        return super().form_valid(form)


class ChirpUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'post_edit.html'
    fields = ['body']


class ChirpDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'post_delete.html'
    success_url = reverse_lazy('pages:home')
