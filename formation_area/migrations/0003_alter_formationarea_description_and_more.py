# Generated by Django 4.2.5 on 2023-09-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation_area', '0002_formationarea_image_program_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formationarea',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='formationarea',
            name='name',
            field=models.CharField(max_length=60, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='program',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='programs/'),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=60, verbose_name='name'),
        ),
    ]
