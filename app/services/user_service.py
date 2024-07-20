from app.db.queries.user_queries import UserQueries
from app.db.queries.poll_queries import PollQueries
from app.models import User


class UserService:

    def get_all_users(self):
        try:
            users = UserQueries.get_all()
            return {"success": True, "data": users}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_user_by_cpf(self, cpf):
        try:
            user = UserQueries.get_where('cpf', cpf)
            return {"success": True, "data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_user_by_email(self, email):
        try:
            user = UserQueries.get_where('email', email)
            return {"success": True, "data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_user_by_username(self, username):
        try:
            user = UserQueries.get_where('username', username)
            return {"success": True, "data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_user_by_id(self, id):
        try:
            user = UserQueries.get_where('id', id)
            return {"success": True, "data": user[0]}
        except Exception as e:
            return {"success": False, "error": str(e)}


    def create_user(self, data):
        try:
            data['role'] = 'USER'
            data['status'] = 'INACTIVE'
            data['is_active'] = 'True'
            data['is_staff'] = 'True'
            data['is_admin'] = 'True'

            user = UserQueries.insert(data)
            return {"success": True, "data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}


    def update_user(self, user, data):
        try:
            user = UserQueries.update(user, data)
            return {"success": True, "data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}


    def get_poll_user(self, user):
        try:
            polls = UserQueries.get_poll(user)
            return {"success": True, "data": polls}
        except Exception as e:
            return {"success": False, "error": str(e)}
        
    def get_polls_by_creator_id(self, creator_id):
        try:
            polls = PollQueries.get_by_creator_id(creator_id)
            total_polls = len(polls)
            return {"success": True, "total_polls": total_polls, "data": polls}
        except Exception as e:
            return {"success": False, "error": str(e)}
        
    
    def password_update(self, user_data, request_data):

        try:
            user = UserQueries.password_update(user_data, request_data) 
            return {"success": True, "request_data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}
        
        
        current_password = request_data['current_password']
        new_password = request_data['new_password']
        
        # Lógica para verificar a senha atual e atualizar para a nova senha
        user = User.objects.get(id=user_data['id'])  # Exemplo: busque o usuário por ID
        
        if not user.check_password(current_password):
            return {'success': False, 'error': 'Senha atual incorreta'}
        
        user.set_password(new_password)  # Atualiza a senha
        user.save()  # Salva as alterações

        return {'success': True, 'data': 'Senha atualizada com sucesso'}