from app.db.connection import create_connection
import psycopg2


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
        connection = None
        try:
            connection = create_connection()
            cursor = connection.cursor()
            query = """
                UPDATE app_user 
                SET cpf = %s, 
                    email = %s, 
                    name = %s, 
                    lname = %s, 
                    username = %s, 
                    status = %s, 
                    role = %s, 
                    password = %s, 
                    is_active = %s, 
                    is_staff = %s, 
                    is_admin = %s 
                WHERE id = %s 
                RETURNING *;
            """

            cursor.execute(query, (
                data['cpf'],
                data['email'],
                data['name'],
                data['lname'],
                data['username'],
                data['status'],
                data['role'],
                data['password'],
                data['is_active'],
                data['is_staff'],
                data['is_admin'],
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