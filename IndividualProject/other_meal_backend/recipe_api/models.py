from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(("name"), max_length=255)
    id = models.IntegerField(("id") , primary_key=True)
    minutes = models.IntegerField(("minutes"))
    contributor_id = models.IntegerField(("contributor_id"))
    submitted = models.DateField(("submitted"), max_length=35)
    tags = models.CharField(("tags"), max_length=1024)
    nutrition = models.CharField(("nutrition"), max_length=255)
    n_steps = models.IntegerField(("n_steps"))
    steps = models.CharField(("steps"), max_length=1024)
    description = models.CharField(("description"), max_length=1024)
    ingredients = models.CharField(("ingredients"), max_length=1024)
    n_ingredients = models.IntegerField(("n_ingredients"))
    recipe_id = models.IntegerField(("recipe_id"))
    average_rating = models.FloatField(("average_rating"), max_length=35)
    votes = models.IntegerField(("votes"))
    like = models.IntegerField(("like"))

    def __init__(self, *args, **kwargs):
        super(Recipe, self).__init__(*args, **kwargs)
