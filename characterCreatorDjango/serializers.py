from django.db.models import fields
from rest_framework import serializers

from .models import Character

class CharacterSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Character
        fields = '__all__'