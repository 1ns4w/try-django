# Generated by Django 3.2.5 on 2021-07-26 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]