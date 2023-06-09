# Generated by Django 4.2.1 on 2023-05-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_workspaceassignment_is_counterparty'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='workspace',
            name='token',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='workspace',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
