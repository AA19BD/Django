from rest_framework import serializers
from .models import MainUser, Client, Staff, Courier, Profile, Card


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'phone')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ClientSerializer(MainUserSerializer):
    class Meta:
        model = Client
        fields = MainUserSerializer.Meta.fields + ('address',)


class CourierSerializer(MainUserSerializer):
    class Meta:
        model = Courier
        fields = MainUserSerializer.Meta.fields + ('salary', 'review',)


class StaffSerializer(MainUserSerializer):
    class Meta:
        model = Staff
        fields = MainUserSerializer.Meta.fields + ('salary',)


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bio = serializers.CharField()
    birth_date = serializers.DateField()
    user = MainUserSerializer()

    # class Meta:
    #     model = Profile
    #     fields = ('id', 'bio', 'birth_date', 'user')
