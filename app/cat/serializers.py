from rest_framework import serializers
from core.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['name', 'years_experience', 'salary', 'breed']
        read_only_fields = ['owner']

    def validate_breed(self, value):
        """Custom breed validation"""
        if not Cat().is_valid_breed(value):
            raise serializers.ValidationError(f"The breed '{value}' is not valid.")
        return value
