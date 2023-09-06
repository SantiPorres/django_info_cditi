from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class FormationAreaList(APIView):
    def get(self, request, format=None):
        formation_areas = FormationArea.active.all()
        serializer = FormationAreaSerializer(formation_areas, many=True)
        return Response(serializer.data)
