# Generated by Django 5.0.3 on 2024-03-15 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_test_fx', '0004_members_connection_state_alter_members_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members_test_fx.members'),
        ),
    ]