from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication as auth

from drf_spectacular.utils import extend_schema
from .serializers import LoginSerializer, LoginResponseSerializer
from .models import Account
from rest_framework_simplejwt.tokens import RefreshToken

@extend_schema(
    request=LoginSerializer,
    responses={200: LoginResponseSerializer, 400: None, 404: None},
    tags=["Autenticación"]
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return Response({'error': "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND)

    account = auth.authenticate(username=username, password=password)
        
    if account is not None:
        refresh = RefreshToken.for_user(account)
        data = {
            'username': account.username,
            'email': account.email,
            'nombre': account.nombre,
            'apellido': account.apellido,
            'token': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        }
        return Response(data)
    else:
        return Response({'error': "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
