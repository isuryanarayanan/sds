from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes
import json
from accounts.forms.create_user_profile import (
    CustomerProfileCreationForm,
    VendorProfileCreationForm,
    AdministratorProfileCreationForm
)


class CreateUserProfileEngine():
    """
    Engine creates a standard for request processing, the 
    '__init__()' method saves the incoming request into 
    state and further creates a profile if not created for
    the authenticated user.
    """

    # The incoming request.
    request = None
    # The response to return to the view.
    response = None
    # Profiles
    profiles = {
        1: "CUSTOMER",
        2: "VENDOR",
        3: "ADMINISTRATOR"
    }

    def __init__(self, params):
        # Loading defaults
        self.request = params
        getattr(self, self.profiles[self.request.user.mode])()
        # try:
        #     getattr(self, self.profiles[self.request.user.mode])()
        # except:
        #     self.response = "Error"

    def respond(self):
        # Respond from request.
        return str(self.response)

    def CUSTOMER(self):
        params = {
            "user": self.request.user.id,
            "first_name": json.loads(self.request.body)['first_name'],
            "last_name": json.loads(self.request.body)['last_name']
        }
        f = CustomerProfileCreationForm(data=params)
        if f.is_valid():
            f.save()
            self.response = f.data
        else:
            raise ValidationError("Error creating profile")

    def VENDOR(self):
        print("vendor profile creation")

    def ADMINISTRATOR(self):
        print("vendor profile creation")


class CreateUserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = CreateUserProfileEngine(request)
        # Respond.
        return Response(Engine.respond())

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
