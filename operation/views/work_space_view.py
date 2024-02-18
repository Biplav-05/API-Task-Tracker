from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class WorkSpaceListView(APIView):
    def get(self, request):
        data = request.user.id
        return Response('hii')
    def create(self):
        pass