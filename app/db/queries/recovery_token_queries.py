from app.db.connection import create_connection
import psycopg2

class RecoveryTokenQueries:
    @staticmethod
    def create(code, now, expiration_date, user_id):
        connection = create_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "INSERT INTO app_recoverytoken (token, created_at, expires_at, user_id) VALUES (%s, %s, %s, %s);"
            cursor.execute(query, (code, now, expiration_date, user_id))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error while inserting data into PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Connection to PostgreSQL closed")

    @staticmethod
    def get_by_token(token):
        connection = create_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM app_recoverytoken WHERE token = %s;"
            cursor.execute(query, (token,))
            record = cursor.fetchone()
            return record
        except (Exception, psycopg2.Error) as error:
            print("Error while selecting data from PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Connection to PostgreSQL closed")