from rest_framework import serializers
from .models import FormationArea, ProgramType, Program


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'id',
            'name',
            'get_absolute_url',
        )


class ProgramTypeSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True)
    
    class Meta:
        model = ProgramType
        fields = (
            'type',
            'programs'
        )

class FormationAreaSerializer(serializers.ModelSerializer):
    program_types = ProgramTypeSerializer(many=True)

    class Meta:
        model = FormationArea
        fields = (
            'id',
            'name',
            'description',
            'slug',
            'get_image',
            'get_absolute_url',
            'program_types'
        )