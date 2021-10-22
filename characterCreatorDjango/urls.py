from django.urls import path
from . views import CharacterView, CurrentUser, CreateUserView, CharacterDetails
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('characters/', CharacterView.as_view(), name='characters_view'),
    path('characters/<str:name>', CharacterDetails.as_view(), name='characters_detail_view'),
    path('user/', CurrentUser.as_view(), name='current_user_view'),
    path('create/', CreateUserView.as_view(), name='create_user_view'),
]