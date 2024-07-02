from app.db.factories.user_factory import UserFactory
from app.db.factories.poll_factory import PollFactory
from app.db.factories.option_factory import OptionFactory
from app.db.factories.question_field_factory import QuestionFieldFactory
from app.models.user_model import User

class DatabaseSeeder:

    def __init__(self):
        pass

    def seed(self):
        self.create_admin_user()
        self.seed_users()
        self.seed_polls()

    def seed_users(self):
        users = UserFactory.create_batch(10)
        for user in users:
            user.save()

    def seed_polls(self):
        polls = PollFactory.create_batch(10)
        for poll in polls:
            poll.save()

            # Criar pelo menos um QuestionField para cada Poll
            question_field = QuestionFieldFactory(poll=poll)
            question_field.save()

            # Criar pelo menos uma Option para cada QuestionField
            option = OptionFactory(question=question_field)
            option.save()

    def create_admin_user(self):
        admin = User(
            cpf='00000000000',
            email='admin@vota.ai',
            name='Admin',
            lname='Vota',
            username='admin',
            status='ACTIVE',
            role='MODERATOR',
            password='admin',
            is_admin=True,
            is_staff=True)
        admin.save()



if __name__ == "__main__":
    dbs = DatabaseSeeder()
    dbs.seed()
