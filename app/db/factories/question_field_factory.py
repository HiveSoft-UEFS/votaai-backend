import factory
from factory.django import DjangoModelFactory
from app.models import QuestionField, Poll


class QuestionFieldFactory(DjangoModelFactory):
    class Meta:
        model = QuestionField

    title = factory.Faker('sentence')
    max_qtd_choices = 1
    poll = factory.SubFactory('app.db.factories.poll_factory.PollFactory')
