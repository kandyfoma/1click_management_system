# Generated by Django 3.2.16 on 2022-11-21 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='cree_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cree_par_stock', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stock',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.produit'),
        ),
        migrations.AddField(
            model_name='stock',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_stock', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='saison',
            name='cree_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cree_par_saison', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='saison',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_saison', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='produit',
            name='cree_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cree_par_produit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='produit',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_produit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='finance',
            name='cree_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cree_par_finance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='finance',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_finance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='departement',
            name='cree_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cree_par_departement', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='departement',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_departement', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delivery',
            name='commande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.commande'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='cree_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cree_par_delivery', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delivery',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_delivery', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commande',
            name='cree_par',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cree_par_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commande',
            name='departement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.departement'),
        ),
        migrations.AddField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.produit'),
        ),
        migrations.AddField(
            model_name='commande',
            name='revendeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.revendeur'),
        ),
        migrations.AddField(
            model_name='commande',
            name='saison',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.saison'),
        ),
        migrations.AddField(
            model_name='commande',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_order', to=settings.AUTH_USER_MODEL),
        ),
    ]
