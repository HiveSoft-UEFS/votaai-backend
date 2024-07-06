from app.db.queries.user_queries import UserQueries
from django.core.mail import send_mail
from django.conf import settings
import random
import requests

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
            data['is_active'] = 'False'
            data['is_staff'] = 'False'
            data['is_admin'] = 'False'

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

    def recover_password(self, email):
        try:
            user = UserQueries.get_where('email', email)
            print("oioi")
            if len(user) != 0:
                first_user = user[0]
                email = first_user.get('email')  # Ou email = first_user['email']
                print(email)
                
            else:
                print("A lista de usuários está vazia.")
                return {"success": False, "error": 'Usuário não encontrado.'}
            secret = random.randint(100000, 999999)
            subject = 'Recuperação de senha.'
            message = 'Use esse código para renovar sua senha: '+ str(secret)
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

           
            requests.post(
                "https://api.mailgun.net/v3/sandbox2cfe3ff8cb0a4360a6bda7c93f8e4067.mailgun.org/messages",
                auth=("api", "YOUR_API_KEY"),
                data={"from": "Excited User <mailgun@sandbox2cfe3ff8cb0a4360a6bda7c93f8e4067.mailgun.org>",
                    "to": ['hivesoft.uefs@gmail.com'],
                    "subject": "Hello",
                    "text": "Testing some Mailgun awesomeness!"})

            send_mail(subject, message, email_from, recipient_list)
            return {"success": True, "data": secret}

        except Exception as e:
            return {"success": False, "error": str(e)}
        
        
        
