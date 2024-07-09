from app.db.connection import create_connection
import psycopg2


class VoteQueries:
    @staticmethod
    def getVote(hash):

        cursor = create_connection().cursor()
        if not cursor:
            return

        try:

            cursor.execute("SELECT id FROM app_vote WHERE hash = %s", [hash])
            row_vote = cursor.fetchone()
            if not row_vote:
                return None

            vote_id = row_vote[0]


            cursor.execute("SELECT id FROM app_choice WHERE vote_id = %s", [vote_id])
            row_choice = cursor.fetchone()
            if not row_choice:
                return None

            choice_id = row_choice[0]


            cursor.execute("SELECT option_id FROM app_choice WHERE id = %s", [choice_id])
            row_option = cursor.fetchone()

            if not row_option:
                return None

            option_id = row_option[0]


            cursor.execute("SELECT question_id FROM app_option WHERE id = %s", [option_id])
            row_question = cursor.fetchone()

            if not row_question:
                return None

            question_id = row_question[0]

            cursor.execute("SELECT poll_id FROM app_questionfield WHERE id = %s", [question_id])
            row_poll = cursor.fetchone()

            if not row_poll:
                return None

            poll_id = row_poll[0]

            cursor.execute("SELECT creator_id FROM app_poll WHERE id = %s", [poll_id])
            row_creator = cursor.fetchone()

            if not row_creator:
                return None

            creator_id = row_creator[0]
            cursor.execute("SELECT username FROM app_user WHERE id = %s", [creator_id])
            creator_name = cursor.fetchone()[0]


            cursor.execute("SELECT criation_date, finish_date, status, title, description FROM app_poll WHERE id = %s", [poll_id])
            poll_details = cursor.fetchone()

            if not poll_details:
                return None

            creation_date = poll_details[0]
            finish_date = poll_details[1]
            status_poll = poll_details[2]
            title = poll_details[3]
            description = poll_details[4]

            cursor.execute("SELECT id, title FROM app_questionfield WHERE poll_id = %s", [poll_id])
            questions = []
            rows_questions = cursor.fetchall()

            for row_question in rows_questions:
                question_id = row_question[0]
                question_title = row_question[1]

                cursor.execute("SELECT text FROM app_option WHERE question_id = %s", [question_id])
                options = []
                rows_options = cursor.fetchall()

                for row_option in rows_options:
                    option_text = row_option[0]
                    options.append({
                        'text': option_text
                    })

                questions.append({
                    'title': question_title,
                    'options': options,
                })


            response_data = {
                'creator_name': creator_name,
                'creation_date': creation_date,
                'finish_date': finish_date,
                'status': status_poll,
                'title': title,
                'description': description,
                'questions': questions,
            }

            return response_data
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL", error)
        finally:
            if cursor:
                cursor.connection.close()
                print("Conexão com o PostgreSQL encerrada")


    @staticmethod
    def get_all():
        cursor = create_connection().cursor()
        if not cursor:
            return

        try:
            cursor.execute("SELECT * FROM app_vote")
            votes = cursor.fetchall()
            return votes
        except (Exception, psycopg2.Error) as error:
            print("Erro ao buscar dados no PostgreSQL", error)
        finally:
            if cursor:
                cursor.connection.close()
                print("Conexão com o PostgreSQL encerrada")

    @staticmethod
    def createChoice(idOption,idVote):
        try:
            connection = create_connection()
            cursor =connection.cursor()
            if not cursor:
                return
            querry = "INSERT INTO app_choice (option_id,vote_id) VALUES (%s, %s) RETURNING *;"
            cursor.execute(querry, (idOption,idVote))
            connection.commit()
            column_names = [desc[0] for desc in cursor.description]
            choice_data = cursor.fetchone()
            if choice_data:
                return dict(zip(column_names, choice_data))
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
    def createVote(date):
        try:
            connection = create_connection()
            cursor =connection.cursor()
            if not cursor:
                return
            querry = "INSERT INTO app_vote (date, hash) VALUES (%s, %s) RETURNING *;"
            cursor.execute(querry,(date,'NULL'))
            connection.commit()
            column_names = [desc[0] for desc in cursor.description]
            vote = cursor.fetchone()
            if vote:
                return dict(zip(column_names, vote))
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
    def updateVoteHash(hash,id_vote):
        try:
            connection = create_connection()
            cursor =connection.cursor()
            if not cursor:
                return
            querry = "UPDATE app_vote SET hash = %s WHERE id = %s RETURNING *;"
            cursor.execute(querry,(hash,id_vote))
            connection.commit()
            column_names = [desc[0] for desc in cursor.description]
            vote = cursor.fetchone()
            if vote:
                return dict(zip(column_names, vote))
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Erro ao atualizar dados no PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")


    def getLastVote():
        try:
            connection = create_connection()
            cursor =connection.cursor()
            if not cursor:
                return
            querry = "SELECT * FROM app_vote ORDER BY id DESC LIMIT 1;"
            cursor.execute(querry)

            column_names = [desc[0] for desc in cursor.description]
            vote = cursor.fetchone()
            if not vote:
                return None
            if vote:
                return dict(zip(column_names, vote))
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Erro ao atualizar dados no PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")



    def createParticipation(user,poll):
        try:
            connection = create_connection()
            cursor =connection.cursor()
            if not cursor:
                return
            querry = "INSERT INTO app_participation (user_id, poll_id) VALUES (%s, %s) RETURNING *;"
            cursor.execute(querry,(user,poll))
            connection.commit()
            column_names = [desc[0] for desc in cursor.description]
            participation = cursor.fetchone()
            if participation:
                return dict(zip(column_names, participation))
            else:
                return None
        except (Exception, psycopg2.Error) as error:
            print("Erro ao inserir dados no PostgreSQL:", error)
            raise
        finally:
            if connection:
                connection.close()
                print("Conexão com o PostgreSQL encerrada")