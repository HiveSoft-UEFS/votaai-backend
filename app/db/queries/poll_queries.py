from app.db.connection import create_connection
import psycopg2


class PollQueries:

    @staticmethod
    def get_all():
        connection = create_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM app_poll;"
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
