import factory
from factory.django import DjangoModelFactory
from app.models import Participation
from app.factories import UserFactory, PollFactory  # Ajuste o caminho conforme necessário

class ParticipationFactory(DjangoModelFactory):
    class Meta:
        model = Participation

    user = factory.SubFactory(UserFactory)  # Gera um usuário aleatório
    poll = factory.SubFactory(PollFactory)  # Gera uma votação aleatória
