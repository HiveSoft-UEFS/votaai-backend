from app.db.connection import create_connection
import psycopg2
from werkzeug.security import check_password_hash, generate_password_hash


class UserQueries:

    @staticmethod
    def get_all():
        connection = create_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM app_user;"
            cursor.execute(query)
            column_names = [desc[0] for desc in cursor.description]
            users = cursor.fetchall()
            return [dict(zip(column_names, user)) for user in users]
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL", error)
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")

    @staticmethod
    def get_where(type, value):
        query = ""
        if type == 'cpf':
            query = "SELECT * FROM app_user WHERE cpf = %s;"
        elif type == 'email':
            query = "SELECT * FROM app_user WHERE email = %s;"
        elif type == 'username':
            query = "SELECT * FROM app_user WHERE username = %s;"
        elif type == 'id':
            query = "SELECT * FROM app_user WHERE id = %s;"
        else:
            query = "SELECT * FROM app_user;"

        connection = None
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query, (value,))
            column_names = [desc[0] for desc in cursor.description]
            users = cursor.fetchall()
            return [dict(zip(column_names, user)) for user in users]
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL:", error)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def insert(user):
        connection = None
        try:
            connection = create_connection()
            cursor = connection.cursor()
            query = "INSERT INTO app_user (cpf, email, name, lname, username, status, role, password, is_active, is_staff, is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;"
            cursor.execute(query, (
            user['cpf'], user['email'], user['name'], user['lname'], user['username'], user['status'], user['role'],
            user['password'], user['is_active'], user['is_staff'], user['is_admin']))
            connection.commit()
            column_names = [desc[0] for desc in cursor.description]
            user_data = cursor.fetchone()
            if user_data:
                return dict(zip(column_names, user_data))
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados no PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")

    @staticmethod
    def update(user, data):
        print(data)
        print("entrou em alterar email")
        connection = None
        try:
            connection = create_connection()
            cursor = connection.cursor()
            query = """
                UPDATE app_user 
                SET
                    email = %s, 
                    username = %s    
                WHERE id = %s 
                RETURNING *;
            """

            cursor.execute(query, (
                
                data['email'],
                data['username'],      
                user['id']
            ))

            connection.commit()

            column_names = [desc[0] for desc in cursor.description]
            user_data = cursor.fetchone()
            if user_data:
                return dict(zip(column_names, user_data))
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Erro ao atualizar dados no PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")

    @staticmethod
    def password_update(user, data):
        print('Entrou em mudar senha')
        current_password = data.get('current_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        # Verificar se todas as senhas foram fornecidas
        if not current_password or not new_password or not confirm_password:
            return {'success': False, 'error': 'Todas as senhas devem ser fornecidas.'}

        # Verificar se a nova senha e a confirmação da nova senha coincidem
        if new_password != confirm_password:
            return {'success': False, 'error': 'A nova senha e a confirmação da nova senha não coincidem.'}

        connection = None
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # Buscar a senha atual do usuário no banco de dados
            query = "SELECT password FROM app_user WHERE id = %s;"
            cursor.execute(query, (user['id'],))
            stored_password = cursor.fetchone()[0]

            # Verificar se a senha atual está correta
            if not check_password_hash(stored_password, current_password):
                return {'success': False, 'error': 'A senha atual está incorreta.'}

            # Atualizar para a nova senha
            hashed_new_password = generate_password_hash(new_password)
            update_query = """
                UPDATE app_user 
                SET password = %s
                WHERE id = %s 
                RETURNING *;
            """

            cursor.execute(update_query, (
                hashed_new_password,
                user['id']
            ))

            connection.commit()

            column_names = [desc[0] for desc in cursor.description]
            user_data = cursor.fetchone()
            if user_data:
                return {'success': True, 'data': dict(zip(column_names, user_data))}
            else:
                return {'success': False, 'error': 'Erro ao atualizar a senha.'}
        except (Exception, psycopg2.Error) as error:
            print("Erro ao atualizar a senha no PostgreSQL:", error)
            return {'success': False, 'error': 'Erro ao atualizar a senha no banco de dados.'}
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")
               
              
    @staticmethod
    def partial_update(user, data):
        connection = None
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # Step 1: Initialize the lists
            set_clauses = []
            values = []

            # Step 2: Construct the SET clause and values list
            for key, value in data.items():
                set_clauses.append(f"{key} = %s")
                values.append(value)

            # Step 3: Join the SET clauses
            set_clause = ", ".join(set_clauses)

            # Step 4: Construct the final query
            query = f"""
                UPDATE app_user
                SET {set_clause}
                WHERE id = %s
                RETURNING *;
            """

            # Execute the query with the values and the user's id
            cursor.execute(query, values + [user['id']])
            connection.commit()

            column_names = [desc[0] for desc in cursor.description]
            user_data = cursor.fetchone()
            if user_data:
                return dict(zip(column_names, user_data))
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Erro ao atualizar dados no PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")