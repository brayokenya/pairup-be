# Generated by Django 3.0.8 on 2020-07-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_name',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]