# Generated by Django 4.1.7 on 2023-02-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='mod',
            field=models.CharField(max_length=100),
        ),
    ]
