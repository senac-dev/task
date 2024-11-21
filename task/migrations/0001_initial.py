# Generated by Django 4.2.16 on 2024-11-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tarefa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("concluida", models.BooleanField(default=False)),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
