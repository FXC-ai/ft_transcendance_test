# Generated by Django 5.0.3 on 2024-03-15 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_test_fx', '0003_members_active_members_age_members_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='connection_state',
            field=models.CharField(choices=[('hors ligne', 'Hors Ligne'), ('online', 'Online')], default='hors ligne', max_length=10),
        ),
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)]),
        ),
    ]
