# Generated by Django 3.2 on 2021-04-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='b_id',
            field=models.CharField(max_length=50),
        ),
    ]
