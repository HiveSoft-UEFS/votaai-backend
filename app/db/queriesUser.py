from .connection import create_connection
import psycopg2

def insert_user(user):
    connection = create_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO app_user (cpf, email, name, lname, username, status, role, password, is_active, is_staff, is_admin)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (
            user['cpf'], user['email'], user['name'], user['lname'], user['username'], 
            user['status'], user['role'], user['password'], True, False, False
        ))
        connection.commit()
        print("Dados inseridos com sucesso!")
    except (Exception, psycopg2.Error) as error:
        print("Erro ao inserir dados no PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o PostgreSQL encerrada")
