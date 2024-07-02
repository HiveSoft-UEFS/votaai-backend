import factory
from factory.django import DjangoModelFactory
from app.models import Poll, User


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Poll

    criation_date = factory.Faker('date')
    finish_date = factory.Faker('date')
    status = 'OPEN'
    title = factory.Faker('sentence')
    description = factory.Faker('sentence')
    privacy = factory.Faker('random_element', elements=['PUBLIC', 'RESTRICTED'])
    creator = factory.Faker('random_element', elements=User.objects.all())