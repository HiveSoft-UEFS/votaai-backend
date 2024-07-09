import factory
import random
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
    if privacy == 'RESTRICTED': code = factory.Faker('pyint', min_value=1, max_value=32767)
    category = factory.Faker('random_element', elements=['random','entertainment','tourism','art','culture'])
    tags = factory.Faker('random_element', elements=['#python', '#onepiece', '#saojoao', '#eita', '#nossa',  '#banana'])
    print(privacy,'\n\n')