# Generated by Django 2.2.11 on 2020-04-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('Guru', '0001_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soal',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('user_made', models.IntegerField()),
                ('Soal', models.TextField(max_length=500)),
                ('jawab1', models.CharField(max_length=128)),
                ('jawab2', models.CharField(max_length=128)),
                ('jawab3', models.CharField(max_length=128)),
                ('jawab4', models.CharField(max_length=128)),
                ('sbenar', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'soal',
            },
        ),
        migrations.CreateModel(
            name='Kunci',
            fields=[
                ('kid', models.AutoField(primary_key=True, serialize=False)),
                ('A', models.CharField(max_length=20)),
                ('B', models.CharField(max_length=20)),
                ('C', models.CharField(max_length=20)),
                ('D', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'kunci',
            },
        ),
    ]
