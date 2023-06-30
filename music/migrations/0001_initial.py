# Generated by Django 4.2.2 on 2023-06-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('release_year', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]