# Generated by Django 2.2 on 2020-12-14 13:18

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCli',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_nom', models.CharField(max_length=100, null=True, verbose_name='Nom')),
                ('cli_prenom', models.CharField(max_length=100, null=True, verbose_name='Prénom')),
                ('cli_situation', models.CharField(choices=[('Marié (e)', 'Marié (e)'), ('Divorcé (e)', 'Divorcé (e)'), ('Célibataire', 'Célibataire'), ('Séparé (e)', 'Séparé (e)'), ('Veuf (ve)', 'Veuf (ve)')], max_length=100, null=True, verbose_name='Situation matrimoniale')),
                ('cli_contact', models.CharField(max_length=100, null=True, verbose_name='Contact')),
                ('cli_email', models.EmailField(max_length=100, null=True, verbose_name='Email')),
                ('cli_noumber_of_pesons', models.IntegerField(blank=True, null=True, verbose_name='Nombre de personne dans le foyer')),
                ('cli_adresse_professionnelle', models.CharField(max_length=100, null=True, verbose_name='Adresse professionnelle')),
                ('cli_pays', django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Pays')),
                ('cli_ville', models.CharField(max_length=100, null=True, verbose_name='Ville')),
                ('cli_lieu_recherche', models.CharField(max_length=100, null=True, verbose_name='Lieu de recherche')),
                ('cli_type_bien', models.CharField(help_text='Maison ou Appart et taille', max_length=100, verbose_name='Type de bien')),
                ('cli_pack', models.CharField(choices=[('pack dossier', 'pack dossier'), ('pack visites', 'pack visites')], max_length=100, null=True, verbose_name='Pack')),
                ('cli_budget', models.DecimalField(decimal_places=0, max_digits=8, null=True, verbose_name='Budget alloué')),
                ('cli_salaire_total', models.DecimalField(decimal_places=0, max_digits=8, null=True, verbose_name='Salaire total du foyer')),
                ('cli_montant_declare', models.DecimalField(decimal_places=0, max_digits=8, null=True, verbose_name="Montant declaré sur le dernier avis d'import")),
                ('cli_type', models.CharField(choices=[('visites substituées', 'visites substituées'), ('visites physiques', 'visites physiques')], max_length=100, null=True, verbose_name='Type visite')),
                ('cli_horaire_debut', models.TimeField(null=True, verbose_name='Heure début: créneau horaire de visite')),
                ('cli_horaire_fin', models.TimeField(null=True, verbose_name='Heure fin: créneau horaire de visite')),
                ('cli_motif', models.TextField(null=True, verbose_name='Motif de déménagement')),
                ('cli_document_avis', models.FileField(null=True, upload_to='documents/', verbose_name="Pièce 1: Avis d'impot, attestation d'emplyeur ou contrat de travail")),
                ('cli_document_paye', models.FileField(null=True, upload_to='documents/', verbose_name="Pièce 2: 3 dernières fiches de payes, pièces d'identité")),
                ('cli_document_quittance', models.FileField(null=True, upload_to='documents/', verbose_name='Pièce 3: 3 dernières quittance de loyers')),
                ('cli_decision_ok', models.BooleanField(blank=True, null=True, verbose_name='Décision')),
                ('cli_decision_reunion', models.BooleanField(blank=True, null=True, verbose_name='Reunion')),
            ],
            options={
                'verbose_name': 'Client',
                'db_table': 'client_cli',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlanningPla',
            fields=[
                ('pla_id', models.AutoField(primary_key=True, serialize=False)),
                ('pla_intitule', models.CharField(max_length=100, unique=True, verbose_name='Jour')),
            ],
            options={
                'verbose_name': 'Planning',
                'db_table': 'planning_pla',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisiteVit',
            fields=[
                ('vit_id', models.AutoField(primary_key=True, serialize=False)),
                ('vit_commentaire', models.TextField(blank=True, null=True, verbose_name='Commentaire')),
                ('vit_bilan', models.TextField(blank=True, null=True, verbose_name='Bilan de la visite')),
                ('vit_date', models.DateTimeField(blank=True, null=True, verbose_name='Date prevu de la visite')),
                ('cli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='soumission.ClientCli', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Visite',
                'db_table': 'visite_vit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RecommandationNek',
            fields=[
                ('nek_id', models.AutoField(primary_key=True, serialize=False)),
                ('nek_recommandation', models.TextField(blank=True, null=True, verbose_name='Recommandation')),
                ('nek_date_recommandation', models.DateField(auto_now_add=True, null=True, verbose_name='Date')),
                ('nek_decision', models.CharField(choices=[('Ok', 'Ok'), ('Demande de reunion', 'Demande de reunion')], max_length=100, null=True, verbose_name='Decision')),
                ('cli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='soumission.ClientCli', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Recommandation',
                'db_table': 'recommandation_nek',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CommentaireDem',
            fields=[
                ('dem_id', models.AutoField(primary_key=True, serialize=False)),
                ('dem_commentaires', models.TextField(blank=True, null=True, verbose_name='Commentaire')),
                ('dem_date_commentaire', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('dem_decision', models.CharField(choices=[('Ok', 'Ok'), ('Demande de reunion', 'Demande de reunion')], max_length=100, null=True, verbose_name='Decision')),
                ('cli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='soumission.ClientCli', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'db_table': 'commentaire_dem',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='clientcli',
            name='cli_planning',
            field=models.ManyToManyField(to='soumission.PlanningPla', verbose_name='Planning'),
        ),
        migrations.CreateModel(
            name='BilanBil',
            fields=[
                ('bil_id', models.AutoField(primary_key=True, serialize=False)),
                ('bil_commentaire', models.TextField(blank=True, null=True, verbose_name='Bilan semaine')),
                ('bil_date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('cli', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='soumission.ClientCli', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Bilan',
                'db_table': 'bilan_bil',
                'managed': True,
            },
        ),
    ]
