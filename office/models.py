from django.db import models
from utils.models import BaseOfficeModel


class Office(BaseOfficeModel):

    image = models.ImageField(
        upload_to='offices/', 
        blank=True, 
        null=True
    )

    class Meta:
        db_table = 'office'
        verbose_name = 'office'
        verbose_name_plural = 'offices'
        ordering = ['name']

    def get_absolute_url(self):
        return f"/{self.slug}"

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class SubOffice(BaseOfficeModel):
    office = models.ForeignKey(
        Office,
        related_name='sub_offices',
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='sub_offices/', 
        blank=True, 
        null=True
    )

    class Meta:
        db_table = 'sub_office'
        verbose_name = 'sub office'
        verbose_name_plural = 'sub offices'
        ordering = ['name']

    def get_absolute_url(self):
        return f"/{self.office}/{self.slug}"

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    

class EntrepreneurshipManagement(BaseOfficeModel):
    name = models.CharField(
        max_length=200
    )

    description = models.TextField(max_length=600)

    applications = models.TextField(
        max_length=900,
        blank=True,
        null=True
    )

    comments = models.TextField(
        max_length=300,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='entrepreneurship_management/',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'entrepreneurship_management'
        verbose_name = 'entrepreneurship management'
        ordering = ['name']

    def get_absolute_url(self):
        return f"/{self.slug}"

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class WelfareApprentice(BaseOfficeModel):
    name = models.CharField(
        max_length=100
    )

    aditional_info_current = models.TextField(
        max_length=1500,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='welfare_apprentice/',
        blank=True, 
        null=True
    )

    class Meta:
        db_table = 'welfare_apprentice'
        verbose_name = 'welfare apprentice'
        ordering = ['name']

    def get_absolute_url(self):
        return f"/{self.slug}"

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
