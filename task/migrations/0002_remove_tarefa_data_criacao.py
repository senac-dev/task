# Generated by Django 4.2.16 on 2024-11-21 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tarefa",
            name="data_criacao",
        ),
    ]
