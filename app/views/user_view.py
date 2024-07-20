from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from app.serializers.user_serializer import UserSerializer
from app.serializers.full_user_serializer import FullUserSerializer
from app.services.user_service import UserService
from app.services.email_service import EmailService
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from django.contrib.auth.models import User


#from app.serializers.ChangePasswordSerializer import ChangePasswordSerializer



class UserViewSet(viewsets.ViewSet):
    _service = UserService()

    def get_permissions(self):
        if self.action in ['list', 'create']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    # GET
    def list(self, request):
        users = self._service.get_all_users()
        if users['success']:
            return Response(users['data'], status=status.HTTP_200_OK)
        return Response({'error': users['error']}, status=status.HTTP_404_NOT_FOUND)

    # GET
    def retrieve(self, request, pk=None):
        if not pk:
            return Response({'error': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)

        if str(pk).isdigit():
            if len(str(pk)) == 11:
                user = self._service.get_user_by_cpf(pk)
            else:
                user = self._service.get_user_by_id(pk)
        else:
            if '@' in str(pk):
                user = self._service.get_user_by_email(pk)
            else:
                user = self._service.get_user_by_username(pk)

        if user['success']:
            return Response(user['data'], status=status.HTTP_200_OK)

        return Response({'error': user['error']}, status=status.HTTP_404_NOT_FOUND)

    # POST
    def create(self, request):
        serializer = FullUserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = self._service.create_user(serializer.data)
            if user['success']:
                return Response(user['data'], status=status.HTTP_201_CREATED)
            return Response({'error': user['error']}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT
    def update(self, request, pk=None):
        if not pk:
            return Response({'error': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)

        user = self._service.get_user_by_id(pk)
        if user['success']:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = self._service.update_user(user['data'], serializer.data)
                if user['success']:
                    return Response(user['data'], status=status.HTTP_200_OK)
                return Response({'error': user['error']}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': user['error']}, status=status.HTTP_404_NOT_FOUND)
    
    # PATCH
    def partial_update(self, request, pk=None):
        if not pk:
            return Response({'error': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)

        user = self._service.get_user_by_id(pk)
        if user['success']:
            serializer = UserSerializer(user['data'], data=request.data, partial=True)
            if serializer.is_valid():
                updated_user = self._service.update_user(user['data'], serializer.validated_data)
                if updated_user['success']:
                    return Response(updated_user['data'], status=status.HTTP_200_OK)
                return Response({'error': updated_user['error']}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': user['error']}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['patch'], url_path='change-password', permission_classes=[IsAuthenticated])
    def partial_update_password(self, request, pk=None):
        if not pk:
            return Response({'error': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)

        user = self._service.get_user_by_id(pk)
        if user['success']:
            serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()  # Atualiza a senha no banco
                return Response({'success': 'Senha atualizada com sucesso'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': user['error']}, status=status.HTTP_404_NOT_FOUND)
    # DELETE
    def destroy(self, request, pk=None):
        return Response({'error': 'Not Implemented'})

    @action(detail=False, methods=['get', 'patch'], url_path='profile', permission_classes=[IsAuthenticated])
    def user_profile(self, request):
        user_id = request.user.id  # Usa o ID do usuário autenticado
        user = self._service.get_user_by_id(user_id)

        if request.method == 'GET':
            if user['success']:
                return Response(user['data'], status=status.HTTP_200_OK)
            return Response({'error': user['error']}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': user['error']}, status=status.HTTP_404_NOT_FOUND)


class ForgotPasswordView(viewsets.ViewSet):

    def forgot_password(self, request, email):
        _user_service = UserService()
        _email_service = EmailService()
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)

        user = _user_service.get_user_by_email(email)['data']
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        _email_service.send_forgot_password_email(user[0])
        return Response({'success': 'Email sent'}, status=status.HTTP_200_OK)

    def change_password(self, request):
        _user_service = UserService()
        new_password = request.data.get('new_password')
        recovery_code = request.data.get('recovery_code')

        if not new_password or not recovery_code:
            return Response({'error': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)

        user = _user_service.get_by_recovery_token(recovery_code)
        if not user['success']:
            return Response({'error': 'Invalid recovery code'}, status=status.HTTP_400_BAD_REQUEST)

        user = _user_service.partial_update_user(user["data"][0], {'password': new_password})

        if user['success']:
            return Response(user['data'], status=status.HTTP_200_OK)

        return Response({'error': user['error']}, status=status.HTTP_400_BAD_REQUEST)
      
      
        if request.method == 'PATCH':
            if user['success']:
                user_instance = user['data']
                
                if not isinstance(user_instance, User):
                    return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
                print(f"Atualizando senha: {(request.data)}")
                # Atualizar senha se os dados forem fornecidos
                if 'current_password' in request.data and 'new_password' in request.data:
                    
                    serializer = ChangePasswordSerializer(user_instance, data=request.data, partial=True)
                    if serializer.is_valid():
                        password_update = self._service.password_update(user_instance, serializer.validated_data)
                        if password_update['success']:
                            return Response(password_update['data'], status=status.HTTP_200_OK)
                        return Response({'error': password_update['error']}, status=status.HTTP_400_BAD_REQUEST)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                else:
                    # Atualizar email e username
                    serializer = UserSerializer(user_instance, data=request.data, partial=True)
                    if serializer.is_valid():
                        updated_user = self._service.update_user(user_instance, serializer.validated_data)
                        if updated_user['success']:
                            return Response(updated_user['data'], status=status.HTTP_200_OK)
                        return Response({'error': updated_user['error']}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'error': user['error']}, status=status.HTTP_404_NOT_FOUND)
