from app.db.queries.user_queries import UserQueries
from app.db.factories.user_factory import UserFactory


class DatabaseSeeder:
    @staticmethod
    def seed():
        DatabaseSeeder.seed_users()

    @staticmethod
    def seed_users():
        users = UserFactory.create_batch(10)

        for user in users:
            UserQueries.insert_user(user)


if __name__ == "__main__":
    DatabaseSeeder.seed()
