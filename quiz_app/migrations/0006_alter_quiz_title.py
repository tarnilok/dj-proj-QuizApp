# Generated by Django 3.2.9 on 2021-12-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0005_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=30, unique=True, verbose_name='Title'),
        ),
    ]