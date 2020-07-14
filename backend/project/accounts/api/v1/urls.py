from django.urls import path, include
from .create_user import CreateUserView
from .create_user_profile import CreateUserProfileView
from .handshake import HandshakeView

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='CreateUserView'),
    path('create_user_profile/', CreateUserProfileView.as_view(),
         name='CreateUserProfileView'),
    path('handshake/', HandshakeView.as_view(), name='HandshakeView')
]
