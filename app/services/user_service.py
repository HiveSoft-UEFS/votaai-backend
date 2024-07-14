from datetime import datetime
from datetime import datetime, timezone

from app.db.queries.recovery_token_queries import RecoveryTokenQueries
from app.db.queries.user_queries import UserQueries


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

    def partial_update_user(self, user, data):
        try:
            user = UserQueries.partial_update(user, data)
            return {"success": True, "data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_by_recovery_token(self, token):
        try:
            token = RecoveryTokenQueries.get_by_token(token)

            expiration_date = token[3]
            if expiration_date < datetime.now(timezone.utc):
                return {"success": False, "error": "Token expired"}

            user_id = token[-1]
            user = UserQueries.get_where('id', user_id)
            return {"success": True, "data": user}
        except Exception as e:
            return {"success": False, "error": str(e)}
