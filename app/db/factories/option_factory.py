import factory
from factory.django import DjangoModelFactory
from faker import Faker
from app.models import QuestionField, Option
from PIL import Image, ImageDraw
import io

fake = Faker()


class OptionFactory(DjangoModelFactory):
    class Meta:
        model = Option

    text = factory.Faker('sentence')
    question = factory.SubFactory('app.db.factories.question_field_factory.QuestionFieldFactory')

    @factory.lazy_attribute
    def img(self):
        # Gerar uma imagem aleatória
        img = Image.new('RGB', (100, 100), color=fake.color())
        d = ImageDraw.Draw(img)
        d.text((10, 10), fake.word(), fill=(255, 255, 255))

        # Converter a imagem para binário
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        return img_byte_arr.getvalue()