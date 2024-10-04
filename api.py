from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_framework_extensions.permissions import IsStaffOrOwner

User = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = (JwtAuthentication,)
    permission_classes = (IsAuthenticated, IsStaffOrOwner)
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk == 'me':
            return self.request.user
        return super().get_object()

    @action(detail=True, methods=['patch'])
    def update_profile(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)