from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Definicion de la vista para users.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        """
        Se limita el acceso si no esta autentificado, excepto si se trata de crear/registrar.
        """
        if self.action in ['list', 'retrieve', 'update', 'destroy']:
            return [IsAuthenticated()]
        elif self.action == 'create':
            return [AllowAny()]
        return super(UserViewSet, self).get_permissions()
    
    def list(self, request, *args, **kwargs):
        """
        Se define la devolucion de todos los usuarios si es admin o solo los datos propios.
        """
        if request.user.is_superuser:
            queryset = self.queryset
        else:
            queryset = CustomUser.objects.filter(id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Se registra un nuevo usuario en el sistema y se validan sus datos para hacerlo.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LogoutViewSet(viewsets.ViewSet):
    """
    Se define el logout del sistema, se colocan los refres token el la black list.
    """
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if self.request.data.get('all'):
            tokens = OutstandingToken.objects.filter(user=request.user)
            for token in tokens:
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})