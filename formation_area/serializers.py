from rest_framework import serializers
from .models import FormationArea, ProgramType, Program


class ProgramDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'id',
            'name',
            'description',
            'get_image',
            'get_absolute_url',
        )

class ProgramListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'id',
            'name',
            'get_absolute_url',
        )


class ProgramTypeSerializer(serializers.ModelSerializer):
    programs = ProgramListSerializer(many=True)
    
    class Meta:
        model = ProgramType
        fields = (
            'type',
            'programs'
        )

class FormationAreaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormationArea
        fields = (
            'id',
            'name',
            'description',
            'slug',
            'get_image',
            'get_absolute_url',
        )

class FormationAreaDetailSerializer(serializers.ModelSerializer):
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