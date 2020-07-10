from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json


class CreateUserView(APIView):
    permission_classes = ()

    def post(self, request):
        content = json.loads(request.body)
        # Create users here

        return Response(content)
