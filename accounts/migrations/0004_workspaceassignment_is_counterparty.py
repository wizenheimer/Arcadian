# Generated by Django 4.2.1 on 2023-05-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_workspace_workspaceassignment_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspaceassignment',
            name='is_counterparty',
            field=models.BooleanField(default=False),
        ),
    ]
