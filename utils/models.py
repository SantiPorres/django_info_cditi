from django.db import models
from uuid import uuid4
from django.db.models.query import QuerySet
from slugify import slugify

class ActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status = BaseModel.Status.ACTIVE)

class BaseModel(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'

    name = models.CharField(
        max_length=60,
        verbose_name='name'
    )

    description = models.TextField(max_length=1500)

    slug = models.SlugField(
        unique=True,
        max_length=100,
        db_index=True,
        editable=False
    )

    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    objects = models.Manager()
    active = ActiveManager()

    def save(self, *args, **kwargs):
        name = slugify(self.name)
        self.slug = f"{name}-{uuid4().hex[:6]}"
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.slug
    

class BaseOfficeModel(BaseModel):
    partners = models.TextField(
        max_length=300,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True