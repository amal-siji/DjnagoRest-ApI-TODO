# Generated by Django 4.2.2 on 2023-06-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_todo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='end',
        ),
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.CharField(max_length=2525),
        ),
    ]
