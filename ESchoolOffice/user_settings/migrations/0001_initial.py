# Generated by Django 3.1.7 on 2021-02-27 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mothertongue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mothertongue_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('religion_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caste_name', models.CharField(max_length=50)),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user_settings.religion')),
            ],
        ),
    ]
