from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from operation.models.work_space import WorkSpace
from operation.serializers.space_serializer import SpaceListSerializer, SpaceCreateSerializer, SpaceDetailSerializer, SpaceUpdateSerializer
from operation.services.space_service import SpaceService
from response.error_response import ErrorResponse

class SpaceListView(APIView):
    def get(self, request, work_space_id):
        space=SpaceService.list(work_space_id)
        serializer=SpaceListSerializer(space, many=True)
        return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, work_space_id):
        # check whether the workspace exist or not
        work_space, error = SpaceService.get_work_space(work_space_id)
        if not work_space:
            return ErrorResponse(errors=error, status_code=400)

        request.data['work_space_id']=work_space_id
        serializer=SpaceCreateSerializer(data=request.data)

        if serializer.is_valid():
            
            data, error=SpaceService.create(data=serializer.validated_data)
            if data:
                serializer=SpaceDetailSerializer(data)
                return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
            
            return ErrorResponse(errors=error, status_code=400)
            
        return Response(data={'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class SpaceDetailView(APIView):
#     def get(self, request, work_space_id):
#         user_id=request.user.id
#         work_space, error=WorkSpaceService.retrive(id=work_space_id, user_id=user_id)

#         if work_space:
#             serializer=WorkSpaceDetailSerializer(work_space, many=True)
#             return Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
        
#         return ErrorResponse(errors=error, status_code=404)

#     def put(self, request, work_space_id):
#         #First checks the workspace with authenticte user exist or not
#         work_space, error=WorkSpaceService.retrive(id=work_space_id,user_id=request.user.id)
#         if error:
#             return ErrorResponse(errors=error, status_code=404)

#         request.data.update({'user_id': request.user.id})

#         serializer=WorkSpaceUpdateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
#         work_space_, error=WorkSpaceService.update(work_space, serializer.validated_data)
#         if work_space_:
#             serializer_=WorkSpaceDetailSerializer(work_space_)
#             return Response(data={'data':serializer_.data}, status=status.HTTP_200_OK)
        
#         return ErrorResponse(errors=error, status_code=400)