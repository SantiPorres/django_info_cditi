from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class FormationAreaList(APIView):
    def get(self, request, format=None):
        formation_areas = FormationArea.active.all()
        serializer = FormationAreaListSerializer(formation_areas, many=True)
        return Response(serializer.data)


class FormationAreaDetail(APIView):
    def get_object(self, formation_area_slug):
        try:
            return FormationArea.active.get(slug=formation_area_slug)
        except FormationArea.DoesNotExist:
            raise Http404

    
    def get(self, request, formation_area_slug, format=None):
        formation_area = self.get_object(formation_area_slug)
        serializer = FormationAreaDetailSerializer(formation_area)
        return Response(serializer.data)
    

class ProgramList(APIView):
    def get(self, request, format=None):
        programs = Program.active.all()
        serializer = ProgramListSerializer(programs, many=True)
        return Response(serializer.data)
        

class ProgramDetail(APIView):
    def get_object(self, formation_area_slug, program_type, program_slug):
        try:
            try:
                FormationArea.active.get(slug=formation_area_slug)    
            except FormationArea.DoesNotExist:
                raise Http404
            
            try:
                ProgramType.objects.get(type=program_type)
            except ProgramType.DoesNotExist:
                raise Http404
            
            return Program.active.get(slug=program_slug)
        except Program.DoesNotExist:
            raise Http404
    
    def get(self, request, formation_area_slug, program_type, program_slug, format=None):
        program = self.get_object(formation_area_slug, program_type, program_slug)
        serializer = ProgramDetailSerializer(program)
        return Response(serializer.data)
