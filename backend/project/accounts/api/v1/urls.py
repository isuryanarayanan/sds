from django.urls import path, include
from .create_user import CreateUserView
from .handshake import HandshakeView

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='CreateUserView'),
    path('handshake/', HandshakeView.as_view(), name='HandshakeView')
]
