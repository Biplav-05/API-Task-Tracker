from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from operation.serializers.work_space_serializer import WorkSpaceListSerializer, WorkSpaceCreateSerializer, WorkSpaceDetailSerializer
from operation.services.work_space_service import WorkSpaceService
from response.error_response import ErrorResponse


class WorkSpaceListView(APIView):

    def get(self, request):
        user_id = request.user.id
        work_spaces=WorkSpaceService.list_workspace(user_id)
        serializer=WorkSpaceListSerializer(work_spaces, many=True)
        return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['user_id']=request.user.id
        serializer=WorkSpaceCreateSerializer(data=request.data)

        if serializer.is_valid():
            
            data, error=WorkSpaceService.create_work_space(data=serializer.data)
            if data:
                serializer=WorkSpaceDetailSerializer(data)
                return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
            
            return ErrorResponse(errors=error)
            
        return Response(data={'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class WorkSpaceDetailView(APIView):
    def get(self, request, work_space_id):
        pass
    def put(self, request, work_space_id):
        pass
    def delete(self, request, work_space_id):
        pass