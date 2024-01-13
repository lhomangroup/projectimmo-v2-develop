# Generated by Django 3.1.6 on 2021-03-17 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0023_diagnostic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostic',
            name='id',
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='annonce',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='annonce.annonce'),
        ),
    ]
