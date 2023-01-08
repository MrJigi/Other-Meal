import http

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Recipe
from .serializers import RecipeSerializer

from .service import recipeService
# Create your views here.
# tempDF = pd.read_csv(r"C:\Users\evald\Documents\GitHub\AIR\backend\air_backend\air_pollution.csv")
# def getAllData():
#     headFile = tempDF.head(10)
#     convertToJson = headFile.to_json(orient="table")
#     convertToJson = json.loads(convertToJson)
#     json.dumps(convertToJson, indent=4)
#     return convertToJson


@api_view(['GET'])
def getBestRated(request):
    recipes = recipeService.getMostAccurate(recipeService)
    return Response(recipes)

@api_view(['GET'])
def getByPrefferance(request):
    recipes = recipeService.getByPrefferance(recipeService)
    return Response(recipes)

@api_view(['GET'])
def getData(request):
    Recipes = Recipe.objects.all()
    serializer = RecipeSerializer(Recipes,many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getAllRecipes(request):
#     # need to get ann array of jason and respond to it
#     airqualityJson = {
#                          "date": "2021-09-25 00:00:00",
#                          "PC4": "5611",
#                          "pm10": "7.86494874954224",
#                          "pm2.5": "4.53152179718018",
#                          "no2": "26.5669228363037",
#                          "no": "17.381550579071",
#                          "so2": "2.3094926917553"
#                      }
#     return Response(airqualityJson)

# @api_view(['GET'])
# def getAllRecipes(request):
#     # need to get ann array of jason and respond to it
#     Recipes = Recipe.objects.all()
#     serializer = RecipeSerializer(Recipes,many=True)
#     return Response(Recipes)

@api_view(['GET'])
def getAllRecipes(request):
    # need to get ann array of jason and respond to it
    item = recipeService.getOneItem(recipeService, 86006)
    # recipeItem = RecipeSerializer(item, many=True)
    # Recipes = Recipe.objects.all()
    # serializer = RecipeSerializer(Recipes,many=True)
    return Response(item)

