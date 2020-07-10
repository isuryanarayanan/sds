from django.urls import path, include
from .create_user import CreateUserView

urlpatterns = [
    path('hello/', CreateUserView.as_view(), name='hello'),
]
