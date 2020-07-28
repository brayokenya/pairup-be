# Generated by Django 3.0.8 on 2020-07-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort_name', models.CharField(max_length=30, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
            options={
                'verbose_name_plural': 'cohort',
            },
        ),
    ]
