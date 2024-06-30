import factory
from factory.django import DjangoModelFactory
from app.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    cpf = factory.Faker('random_int', min=10000000000, max=99999999999)
    email = factory.Faker('email')
    name = factory.Faker('name')
    lname = factory.Faker('last_name')
    username = factory.Faker('user_name')
    status = 'active'
    role = 'user'
    password = factory.Faker('password')
