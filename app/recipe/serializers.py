"""
Serializers for recipe app.
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects."""

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'time_minutes', 'price', 'link',
            'ingredients', 'tags', 'image',
        )
        read_only_fields = ('id',)
