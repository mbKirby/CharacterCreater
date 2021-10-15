from rest_framework import generics
from rest_framework.response import Response

from .models import Character
from . serializers import CharacterSerializer

from rest_framework.permissions import IsAuthenticated


class CharacterView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
