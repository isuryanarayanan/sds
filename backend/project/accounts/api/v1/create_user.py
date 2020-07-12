from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from accounts.forms.create_user import CustomerUserCreationForm


class CreateUserEngine():
    """
    Engine creates a standard for request processing, the 
    '__init__()' method saves the incoming request into 
    state and further checks for the 'utype' and runs the 
    method associated with it.
    """

    # The incoming request.
    request = None
    # The response to return to the view.
    response = None
    # The user type to create
    utype = None
    # Credentials
    username = None
    email = None
    password1 = None
    password2 = None
    # The user
    user = None

    def __init__(self, params):
        # Loading defaults
        self.request = params
        self.utype = json.loads(params.body)['user_type']
        self.username = json.loads(params.body)['username']
        self.email = json.loads(params.body)['email']
        self.password1 = json.loads(params.body)['password1']
        self.password2 = json.loads(params.body)['password2']
        getattr(self, self.utype.upper())()
        # try:
        #     # Only use uppercase names for user methods

        # except AttributeError:
        #     self.response = "user_type invalid"

    def respond(self):
        # Respond from request.
        return str(self.response)

    def create_user(self, params):
        f = CustomerUserCreationForm(params)
        if f.is_valid():
            self.user = f.save()

    def create_profile(self):
        pass

    def CUSTOMER(self):
        """
        Customer users will be created with the username,
        email and the cleaned password. The profiles will 
        be created if the profile_data is provided in the
        request.
        """
        if self.username and self.email and self.password1 and self.password2:
            # Create user
            param = {
                "username": self.username,
                "email": self.email,
                "mode": 1,
                "password1": self.password1,
                "password2": self.password2
            }
            print("create user")
            self.create_user(param)
            self.response = self.user

        try:
            profile_data = json.loads(self.request.body)['profile']
            if profile_data:
                # Create user profile
                print("create user profile")
        except KeyError:
            pass

    def VENDOR(self):
        pass

    def ADMINISTRATOR(self):
        # Since it's a protected view
        # Check for auth before responding.
        pass


class CreateUserView(APIView):
    permission_classes = ()

    def post(self, request):
        # Create the engine.
        Engine = CreateUserEngine(request)
        # Respond.
        return Response(Engine.respond())

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
