from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json


class CreateUserEngine():

    request = ''  # The incoming request.
    response = ''  # The response to return to the view.
    utype = ''  # The user type to create

    def __init__(self, params):
        # Loading defaults
        self.utype = json.loads(params.body)['user_type']
        self.request = params

        getattr(self, self.utype.upper())()

    def respond(self):  # Respond from request.
        return str(self.response)

    def CUSTOMER(self):
        pass

    def VENDOR(self):
        pass

    def ADMINISTRATOR(self):
        # Since it's a protected view
        # Check for auth.
        pass


class CreateUserView(APIView):
    permission_classes = ()

    def post(self, request):
        # Create the engine.
        Engine = CreateUserEngine(request)
        # Respond.
        return Response(Engine.respond())
