# Generated by Django 3.2.9 on 2021-12-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_alter_quiz_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Title'),
        ),
    ]
