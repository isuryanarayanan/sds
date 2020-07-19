# Native imports
import json
# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


class IsCustomerUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.mode == 1)


class CustomerProfileEngine():
    pass


class SetCustomerProfileView(APIView):
    permission_classes = (IsAuthenticated, IsCustomerUser)

    def post(self, request):
        # Create the engine.
        Engine = CreateUserEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
