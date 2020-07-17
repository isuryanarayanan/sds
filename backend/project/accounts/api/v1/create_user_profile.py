# Native imports
import json
# Django Imports
from django.core.exceptions import ValidationError
# Rest Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes
# Importing Forms
from accounts.forms.create_user_profile import (
    CustomerProfileCreationForm,
    VendorProfileCreationForm,
    AdministratorProfileCreationForm
)
# Importing User Profiles
from accounts.models.profiles import (
    customer,
    vendor,
    administrator
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
    response_code = None
    # Profiles
    profiles = {
        1: "CUSTOMER",
        2: "VENDOR",
        3: "ADMINISTRATOR"
    }

    def __init__(self, params):
        # Loading defaults
        self.request = params

        try:
            getattr(self, self.profiles[self.request.user.mode])()
        except:
            self.response = "Error"
            self.response_code = 500

    def CheckUser(self, objs, id):
        customers = objs
        for obj in customers:
            if obj.id == id:
                return False
        return True

    def CUSTOMER(self):
        try:
            # Get parameters from request and organize it into the form format.
            params = {
                "user": self.request.user.id,
                "first_name": json.loads(self.request.body)['first_name'],
                "last_name": json.loads(self.request.body)['last_name']
            }
            # CheckUser returns true if there is no profile created for the request user.
            if self.CheckUser(customer.customer_profile.objects.all(), self.request.user.id):
                # Creates the form instance.
                f = CustomerProfileCreationForm(data=params)
                if f.is_valid():
                    f.save()
                    self.response = f.data
                    self.response_code = 201
                else:
                    raise ValidationError("Error creating profile")
                    self.response = "Error creating profile"
                    self.response_code = 500
            else:
                self.response = "Profile already created"
                self.response_code = 403
        except KeyError:
            self.response = "Invalid parameters"
            self.response_code = 400

    def VENDOR(self):
        try:
            # Get parameters from request and organize it into the form format.
            params = {
                "user": self.request.user.id,
                "calendar": json.loads(self.request.body)['calendar'],
                "timeslot": json.loads(self.request.body)['timeslot'],
            }
            # CheckUser returns true if there is no profile created for the request user.
            if self.CheckUser(vendor.vendor_profile.objects.all(), self.request.user.id):
                # Creates the form instance.
                f = VendorProfileCreationForm(data=params)
                if f.is_valid():
                    f.save()
                    self.response = f.data
                    self.response_code = 201
                else:
                    raise ValidationError("Error creating profile")
                    self.response = "Error creating profile"
                    self.response_code = 500
            else:
                self.response = "Profile already created"
                self.response_code = 403
        except KeyError:
            self.response = "Invalid parameters"
            self.response_code = 400

    def ADMINISTRATOR(self):
        try:
            # Get parameters from request and organize it into the form format.
            params = {
                "user": self.request.user.id,
                "first_name": json.loads(self.request.body)['first_name'],
                "last_name": json.loads(self.request.body)['last_name']
            }
            # CheckUser returns true if there is no profile created for the request user.
            if self.CheckUser(administrator.administrator_profile.objects.all(), self.request.user.id):
                # Creates the form instance.
                f = AdministratorProfileCreationForm(data=params)
                if f.is_valid():
                    f.save()
                    self.response = f.data
                    self.response_code = 201
                else:
                    raise ValidationError("Error creating profile")
                    self.response = "Error creating profile"
                    self.response_code = 500
            else:
                self.response = "Profile already created"
                self.response_code = 403
        except KeyError:
            self.response = "Invalid parameters"
            self.response_code = 400


class CreateUserProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = CreateUserProfileEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
