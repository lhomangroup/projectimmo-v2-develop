# Generated by Django 3.1.6 on 2021-05-03 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0024_auto_20210503_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='commentaire_demaya',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.commentaire_demeya'),
        ),
        migrations.AlterField(
            model_name='file',
            name='commentaire_nek',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.commentaire_nek'),
        ),
    ]
