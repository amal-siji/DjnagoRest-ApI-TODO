# Generated by Django 4.2.2 on 2023-06-14 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_remove_todo_end_alter_todo_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
    ]