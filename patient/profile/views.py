from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from ..user.serializers import UserRegistrationSerializer,FileUploadSerializer
from .models import UserProfile,FileUpload

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'q1': user_profile.q1,
                    'q2': user_profile.q2,
                    'q3': user_profile.q3,
                    'q4': user_profile.q4,
                    'q5': user_profile.q5,
                    'docfile': user_profile.docfile,
                    # 'imgDoc':user_profile.imgDoc,
                    
                    }]
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)


class FileUploadViewSet(ModelViewSet):
    
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                       datafile=self.request.data.get('datafile'))