# Generated by Django 2.2.5 on 2021-09-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_searchengine_search_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchengine',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
