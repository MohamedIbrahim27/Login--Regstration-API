# Generated by Django 4.2 on 2023-11-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_normaluser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
