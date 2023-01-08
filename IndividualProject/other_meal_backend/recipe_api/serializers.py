from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["name", "id", "minutes", "contributor_id", "submitted", "tags", "nutrition","n_steps", "steps", "description", "ingredients","n_ingredients", "recipe_id", "average_rating","votes","like"]
        # fields = ['__all__']