# Generated by Django 4.2.1 on 2023-07-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_word_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]