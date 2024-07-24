from app.db.connection import create_connection
from app.db.connection import close_connection
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
            raise 
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")

    def get_where(type, filter, order, category, value):
        query = ''
        if type == 'code':
            query = (
                "SELECT * FROM app_poll "
                "WHERE code = %s "
                "AND (privacy = 'Restricted' OR privacy = 'RESTRICTED') "
                "AND (status = 'Open' OR status = 'OPEN')"
            )
            param = [str(value)]
        elif (type == 'title' or type == 'tags') and category == 'all':
            query = (
                "SELECT p.* FROM app_poll AS p " 
                "WHERE p." + type + " LIKE %s "
                "AND (p.privacy = 'Public' OR p.privacy = 'PUBLIC') " 
                "AND (p.status = 'Open' OR p.status = 'OPEN') " 
            )
            param = ['%' + value + '%']
        elif (type == 'title' or type == 'tags') and category != 'all':
            query = (
                "SELECT p.* FROM app_poll AS p " 
                "WHERE p." + type + " LIKE %s " 
                "AND (p.privacy = 'Public' OR p.privacy = 'PUBLIC') " 
                "AND (p.status = 'Open' OR p.status = 'OPEN') " 
                "AND p.category LIKE %s " 
            )
            print(query)
            param = ['%' + value + '%','%' + category + '%']
        if(type != 'code' and (order == 'ASC' or order == 'DESC')):
            query = query+("ORDER BY p." + filter + ' ' + order)
        elif(type != 'code' and order == 'pop'):
            query = query.replace(
                "SELECT p.* FROM app_poll AS p ", (
                    "SELECT p.*, COUNT(DISTINCT u.id) AS user_count FROM app_poll p "
                    "LEFT JOIN app_participation AS par ON p.id = par.poll_id "
                    "LEFT JOIN app_user AS u ON par.user_id = u.id "
                )
            )
            query = query+("GROUP BY p.id ORDER BY user_count DESC")
        connection = create_connection()
        if not connection:
            return 
        try:
            cursor = connection.cursor()
            cursor.execute(query, param)
            column_names = [desc[0] for desc in cursor.description]
            polls = [dict(zip(column_names,poll)) for poll in cursor.fetchall()]
            for h in polls:
                cursor.execute("SELECT * FROM app_QuestionField WHERE poll_id = %s ;", (h['id'],))
                column_names = [desc[0] for desc in cursor.description]
                questions =  [dict(zip(column_names, question)) for question in cursor.fetchall()]
                for i in questions:
                    cursor.execute("SELECT * FROM app_option WHERE question_id = %s ;", (i['id'],))
                    column_names = [desc[0] for desc in cursor.description]
                    options =  [dict(zip(column_names, option)) for option in cursor.fetchall()]
                    for j in options:
                        j['img'] = 'DANDO BUG'
                    for i in questions:
                        if i['id'] == options[0]['question_id']:
                            i['options'] = options
                            break
                h['question_field'] = questions
            return polls
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL", error)
        finally:
            close_connection(connection)

    def get_user_polls(user_id):
        connection = create_connection()
        if not connection:
            return

        try:
            cursor = connection.cursor()

            # Consultando votações criadas pelo usuário
            query_created = """
                SELECT id, status, criation_date, title
                FROM app_poll 
                WHERE creator_id = %s;
            """
            cursor.execute(query_created, (user_id,))
            created_polls = cursor.fetchall()

            # Consultando votações participadas pelo usuário
            query_participated = """
                SELECT poll.id, poll.status, poll.criation_date, poll.title 
                FROM app_poll poll
                JOIN app_participation participation ON poll.id = participation.poll_id
                WHERE participation.user_id = %s;
            """
            cursor.execute(query_participated, (user_id,))
            participated_polls = cursor.fetchall()

            polls = []

            # Adicionando as votações criadas ao resultado
            for poll in created_polls:
                polls.append({
                    "status": poll[1],
                    "data_criacao": poll[2],
                    "titulo": poll[3],
                    "tipo": "Criada"
                })

            # Adicionando as votações participadas ao resultado
            for poll in participated_polls:
                polls.append({
                    "status": poll[1],
                    "data_criacao": poll[2],
                    "titulo": poll[3],
                    "tipo": "Participada"
                })

            return {"polls": polls}

        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL", error)
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")

    def get_poll_counts_by_user(user_id):
        connection = create_connection()
        if not connection:
            return {'criadas': 0, 'participadas': 0}
        
        try:
            cursor = connection.cursor()
            
            # Contar polls criadas pelo usuário
            query_created = """
            SELECT COUNT(*) FROM app_poll WHERE creator_id = %s;
            """
            cursor.execute(query_created, [str(user_id)])
            created_count = cursor.fetchone()[0]
            
            # Contar polls participadas pelo usuário
            query_participated = """
            SELECT COUNT(*) FROM app_participation WHERE user_id = %s;
            """
            cursor.execute(query_participated, [str(user_id)])
            participated_count = cursor.fetchone()[0]
            
            return {
                'criadas': created_count,
                'participadas': participated_count
            }
            
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL", error)
            return {'criadas': 0, 'participadas': 0}
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")
