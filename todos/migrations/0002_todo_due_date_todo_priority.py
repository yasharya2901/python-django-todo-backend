# Generated by Django 5.1 on 2024-08-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=0),
        ),
    ]
