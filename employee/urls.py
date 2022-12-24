from django.urls import path
from django.http import HttpResponse
from .views import CreateRegister, SnippetList, TutorList,SubscribeList,TutorRegister, SubscribeRegister


app_name = 'employee'


urlpatterns = [
    path("", lambda request: HttpResponse('Hello World'), name='hello'),
    path('create/', CreateRegister.as_view()),
    path('x/', SnippetList.as_view()),
    path('tutor/', TutorList.as_view()),
    path('tutorx/', TutorRegister.as_view()),
    path('subscribe', SubscribeRegister.as_view()),
    path('subscribex/', SubscribeList.as_view())

]






