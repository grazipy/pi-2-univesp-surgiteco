# Generated by Django 5.1.3 on 2024-11-05 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view_docs_surgitec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='campo_temporario',
        ),
    ]
