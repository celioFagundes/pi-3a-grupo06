# Generated by Django 5.1.7 on 2025-04-27 19:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_resposta', models.DateField()),
                ('pontuacao', models.IntegerField()),
                ('classificacao', models.CharField(choices=[('SEM_SOFRIMENTO', 'Sem Sofrimento'), ('LEVE', 'Leve'), ('MODERADO', 'Moderado'), ('GRAVE', 'Grave')], default='SEM_SOFRIMENTO', max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
