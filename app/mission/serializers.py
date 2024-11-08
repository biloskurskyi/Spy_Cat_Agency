from rest_framework import serializers

from core.models import Goal, Mission


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['name', 'country', 'notes', 'status']


class MissionSerializer(serializers.ModelSerializer):
    goals = GoalSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['name', 'description', 'cat', 'is_completed', 'goals']

    def create(self, validated_data):
        goals_data = validated_data.pop('goals')
        mission = Mission.objects.create(**validated_data)
        for goal_data in goals_data:
            Goal.objects.create(mission=mission, **goal_data)
        return mission
