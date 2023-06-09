# Generated by Django 4.2.1 on 2023-05-29 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_alter_user_workspace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(max_length=255)),
                ('stripe_customer_id', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.workspace')),
            ],
        ),
    ]
