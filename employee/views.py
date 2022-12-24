
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Register, Tutor, Subscribe
from .forms import RegisterForm,TutorForm, SubscribeForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seralizers import AccountSerializer, TutorSerializer, SubscribeSerializer
from django.core.mail import send_mail
from django.conf import settings
from . import mail

subject = 'New Session Booking!'
# emailFrom = "ifeanyi.okala.247238@unn.edu.ng"
recipient_list = "okala_ifeanyi@yahoo.com"
#
# subject = 'welcome to GFG world'
# message = 'Hi {user.username}, thank you for registering in geeksforgeeks.'
# email_from = settings.EMAIL_HOST_USER
# recipient_list = [emailFrom, ]
# send_mail( subject, message, email_from, recipient_list )

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Register.objects.all()
        serializer = AccountSerializer(snippets, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    # def send_book(self,book_data):
    #     message = "A new query has been added in Category" + str(book_data.category)
    #     send_mail(subject, message, settings.EMAIL_HOST_USE, recipient_list, fail_silently=False)
    #     print('sent')
    #

    def post(self, request, format=None):
        subject = 'New Session Booking!'
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            book_data = serializer.save()
            message = "A new query has been added in this Category"
            message += "\n Name: " + book_data.f1name
            message+= "\n Contact: " + str(book_data.email)
            message += "\n Subject: " + str(book_data.phone)
            message += "\n Why they need tutoring: " + str(book_data.why)
            # msg += "\n Address: " + str(query.address)
            # send_mail(subject, message, recipient_list, settings.EMAIL_HOST_USER, fail_silently=False)
            mail.send(subject,message)
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
        subject = 'New Tutor Booking!'
        serializer = TutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            tutor_data = serializer.save()
            message = "A new query has been added in this Category"
            message += "\n Name: " + tutor_data.f1name
            message += "\n Contact: " + str(tutor_data.email)
            message += "\n Subject: " + str(tutor_data.phone)
            message += "\n Tell us about yourself: " + str(tutor_data.you)
            # msg += "\n Address: " + str(query.address)
            # send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
            mail.send(subject,message)
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
        print('=========================')
        subject = 'New Subscriber!'
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            subscribe_data = serializer.save()
            message = "A new query has been added in this Category"
            message += "\n Name: " + subscribe_data.Email
            # message += "\n Contact: " + str(book_data.email)
            # message += "\n Subject: " + str(book_data.phone)
            # message += "\n Why they need tutoring: " + str(book_data.why)
            # msg += "\n Address: " + str(query.address)
            # send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
            mail.send(subject,message)
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


