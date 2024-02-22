from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from operation.serializers.work_space_serializer import WorkSpaceListSerializer, WorkSpaceCreateSerializer, WorkSpaceDetailSerializer, WorkSpaceUpdateSerializer
from operation.services.work_space_service import WorkSpaceService
from response.error_response import ErrorResponse

class WorkSpaceListView(APIView):

    def get(self, request):
        user_id = request.user.id
        work_spaces=WorkSpaceService.list(user_id)
        serializer=WorkSpaceListSerializer(work_spaces, many=True)
        return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['user_id']=request.user.id
        serializer=WorkSpaceCreateSerializer(data=request.data)

        if serializer.is_valid():
            
            data, error=WorkSpaceService.create(data=serializer.data)
            if data:
                serializer=WorkSpaceDetailSerializer(data)
                return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
            
            return ErrorResponse(errors=error)
            
        return Response(data={'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class WorkSpaceDetailView(APIView):
    def get(self, request, work_space_id):
        user_id=request.user.id
        work_space, error=WorkSpaceService.retrive(id=work_space_id, user_id=user_id)

        if work_space:
            serializer=WorkSpaceDetailSerializer(work_space, many=True)
            return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
        
        return ErrorResponse(errors=error, status_code=404)

    def put(self, request, work_space_id):
        #First checks the workspace with authenticte user exist or not
        work_space, error=WorkSpaceService.retrive(id=work_space_id,user_id=request.user.id)
        if error:
            return ErrorResponse(errors=error, status_code=404)

        request.data.update({'user_id': request.user.id})

        serializer=WorkSpaceUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        work_space_, error=WorkSpaceService.update(work_space, serializer.validated_data)
        if work_space_:
            serializer_=WorkSpaceDetailSerializer(work_space_)
            return Response(data={'data':serializer_.data}, status=status.HTTP_200_OK)
        
        return ErrorResponse(errors=error, status_code=400)