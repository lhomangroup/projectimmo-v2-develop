# Generated by Django 3.1.6 on 2021-03-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='verdict',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
