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



    @staticmethod
    def get_by_id(id):
        connection = create_connection()
        if not connection:
            return
        
        try:
            cursor = connection.cursor()

            query = "SELECT * FROM app_poll WHERE id = %s ;"
            params = [str(id)]
            cursor.execute(query, params)
            poll = cursor.fetchone()
            column_names = [desc[0] for desc in cursor.description]
            poll = dict(zip(column_names, poll))




            cursor.execute("SELECT * FROM app_QuestionField WHERE poll_id = %s ;", [str(id)])
            column_names = [desc[0] for desc in cursor.description]
            questions = cursor.fetchall()

            questions =  [dict(zip(column_names, question)) for question in questions]


            for i in questions:
                cursor.execute("SELECT * FROM app_option WHERE question_id = %s ;", [str(i['id'])])
                column_names = [desc[0] for desc in cursor.description]
                options = cursor.fetchall()
                options =  [dict(zip(column_names, option)) for option in options]
                for j in options:
                    j['img'] = 'DANDO BUG'
                for i in questions:
                    if i['id'] == options[0]['question_id']:
                        i['options'] = options
                        break
                
            
            poll['question_field'] = questions
            
            return poll







        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL", error)


        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")

