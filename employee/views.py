from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Register
from .forms import RegisterForm


class CreateRegister(CreateView):
    queryset = Register.objects.all()
    form_class = RegisterForm
    template_name = 'form.html'
    success_url = reverse_lazy('employee:hello')