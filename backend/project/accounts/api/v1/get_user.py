# Native imports
import json
# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


class GetUserEngine():
    # The incoming request.
    request = None
    # The response to return to the view.
    response = None
    response_code = None

    def __init__(self, params):
        # Loading defaults
        self.request = params
        try:
            # self.utype = json.loads(params.body)['user_id']
            print(params.user)
        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400

        try:
            # Only use uppercase names for user methods
            getattr(self, self.utype.upper())()
        except AttributeError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class GetUserView(APIView):
    permission_classes = ()

    def post(self, request):
        # Create the engine.
        Engine = GetUserEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
