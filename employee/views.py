
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Register, Tutor, Subscribe
from .forms import RegisterForm,TutorForm, SubscribeForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seralizers import AccountSerializer, TutorSerializer, SubscribeSerializer




class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Register.objects.all()
        serializer = AccountSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Tutor.objects.all()
        serializer = TutorSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscribeList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Subscribe.objects.all()
        serializer = SubscribeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateRegister(CreateView):
    queryset = Register.objects.all()
    form_class = RegisterForm
    template_name = 'form.html'
    success_url = reverse_lazy('employee:hello')

class TutorRegister(CreateView):
    queryset = Tutor.objects.all()
    form_class = TutorForm
    template_name = 'form.html'
    success_url = reverse_lazy('employee:hello')


class SubscribeRegister(CreateView):
    queryset = Subscribe.objects.all()
    form_class = SubscribeForm
    template_name = 'form.html'
    success_url = reverse_lazy('employee:hello')


