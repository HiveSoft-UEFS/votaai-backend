from rest_framework import serializers
from app.models import Option, QuestionField, Poll

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['text', 'img']

class QuestionFieldSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)


    class Meta:
        model = QuestionField
        fields = ['title', 'max_qtd_choices', 'options']

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionFieldSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['title', 'description', 'finish_date', 'privacy', 'questions', 'criation_date', 'status', 'creator', 'category']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        poll = Poll.objects.create(**validated_data)
        for question_data in questions_data:
            options_data = question_data.pop('options')
            question = QuestionField.objects.create(poll=poll, **question_data)
            for option_data in options_data:
                Option.objects.create(question=question, **option_data)
        return poll
