# Generated by Django 4.2.11 on 2024-10-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_socmajor"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="program_areas",
            field=models.ManyToManyField(
                blank=True, related_name="projects", to="core.programarea"
            ),
        ),
    ]
