from rest_framework import serializers
from employee.models import Register, Tutor, Subscribe


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'

