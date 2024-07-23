import psycopg2
from psycopg2 import OperationalError
import os

def create_connection():
    db_url = os.getenv('DATABASE_URL')
    try:
        connection = psycopg2.connect(db_url)
        return connection
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None