from django.shortcuts import render
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework import viewsets

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()