# Generated by Django 4.2.2 on 2023-06-14 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.AddField(
            model_name='todo',
            name='end',
            field=models.DateTimeField(null=True),
        ),
    ]