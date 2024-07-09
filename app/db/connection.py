import psycopg2
from psycopg2 import OperationalError


def create_connection():
    try:
        connection = psycopg2.connect(
            user="votaai",
            password="votaai",
            host="localhost",
            port="5432",
            database="votaai"
        )
        return connection
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Conexão com o PostgreSQL encerrada")