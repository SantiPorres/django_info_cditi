from django.db import models
from utils.models import BaseModel


class FormationArea(BaseModel):

    class Meta:
        db_table = 'formation_area'
        verbose_name = 'formation area'
        verbose_name_plural = 'formation areas'
        ordering = ['name']

    image = models.ImageField(
        upload_to='formation_areas/', 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return f"/{self.slug}"
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    

class ProgramType(models.Model):
    formation_area = models.ForeignKey(
        FormationArea,
        related_name='program_types',
        on_delete=models.CASCADE
    )

    class Type(models.TextChoices):
        TECHNICAL = 'technical', 'Technical'
        TECHNOLOGIST = 'technologist', 'Technologist'
        OPERATOR = 'operator', 'Operator'
        SPECIALIZATION = 'specialization', 'Specialization'
        ASSISTANT = 'assistant', 'Assistant'

    type = models.CharField(
        max_length=15,
        choices=Type.choices,
        default=Type.TECHNICAL
    )

    class Meta:
        db_table = 'program_type'
        verbose_name = 'program type'
        verbose_name_plural = 'program types'
        ordering = ['type']
        constraints = [
            models.UniqueConstraint(
                fields=['formation_area', 'type'],
                name='unique_program_type'
            )
        ]

    def __str__(self):
        return self.type
    

class Program(BaseModel):

    formation_area = models.ForeignKey(
        FormationArea,
        on_delete=models.CASCADE
    )

    program_type = models.ForeignKey(
        ProgramType,
        related_name='programs',
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='programs/', 
        blank=True, 
        null=True
    )
    
    class Journey(models.TextChoices):
        MORNING = 'morning', 'Morning'
        AFTERNOON = 'afternoon', 'Afternoon'
        NIGHT = 'night', 'Night'

    journey = models.CharField(
        max_length=10,
        choices=Journey.choices,
        default=Journey.MORNING
    )

    class Meta:
        db_table = 'program'
        verbose_name = 'program'
        verbose_name_plural = 'programs'
        ordering = ['name']

    def get_absolute_url(self):
        return f"/{self.formation_area}/{self.program_type}/{self.slug}"
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''