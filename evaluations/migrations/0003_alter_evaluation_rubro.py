# Generated by Django 3.2.3 on 2021-06-05 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0002_alter_evaluation_rubro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='rubro',
            field=models.ForeignKey(default='-', on_delete=django.db.models.deletion.SET_DEFAULT, to='evaluations.rubro'),
        ),
    ]
