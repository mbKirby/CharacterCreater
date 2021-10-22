from rest_framework import generics, serializers
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Character , User
from . serializers import CharacterSerializer , CreateUserSerializer, CurrentUserSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated


class CurrentUser(generics.ListCreateAPIView):
    serializer_class = CurrentUserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.user
        currentuser = queryset.filter(id=user.id)
        print(user)
        return currentuser

class CharacterView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CharacterSerializer
    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(user=user)

class CreateUserView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class CharacterDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='name'
    # permission_classes = (IsAuthenticated,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    