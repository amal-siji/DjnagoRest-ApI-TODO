# Generated by Django 4.2.2 on 2023-06-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_remove_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.IntegerField(default=True, editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
