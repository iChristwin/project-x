from django.forms import ModelForm
from .models import Register, Tutor, Subscribe


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['f1name','email','phone','why']



class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields = ['f1name','email','phone','you']

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['Email']