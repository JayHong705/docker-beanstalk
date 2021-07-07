from rest_framework import serializers

from .models import Poll, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = (
            'choice',
            'poll',
            'voted_by',
        )


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = (
            'poll',
            'choice_text',
            'votes',
        )


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = (
            'user_created',
            'question',
            'choices',
            'created',
        )

    def validate_user_created(self, value):
        return value

    def validate_question(self, value):
        return value

    def validate_choices(self, value):
        return value
