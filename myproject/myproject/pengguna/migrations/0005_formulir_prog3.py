# Generated by Django 5.0.6 on 2024-05-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0004_formulir_delete_formulirform'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulir',
            name='prog3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
