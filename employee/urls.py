from django.urls import path
from django.http import HttpResponse
from .views import CreateRegister

app_name = 'employee'


urlpatterns = [
    path("", lambda request: HttpResponse('Hello World'), name='hello'),
    path('create/', CreateRegister.as_view())
]
