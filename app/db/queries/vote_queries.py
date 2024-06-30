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

                cursor.execute("SELECT text, img FROM app_option WHERE question_id = %s", [question_id])
                options = []
                rows_options = cursor.fetchall()

                for row_option in rows_options:
                    option_text = row_option[0]
                    option_img = row_option[1]
                    options.append({
                        'text': option_text,
                        'img': option_img,
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