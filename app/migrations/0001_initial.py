# Generated by Django 5.0.3 on 2024-03-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=36)),
                ('fam', models.CharField(max_length=36)),
                ('yosh', models.IntegerField()),
                ('login', models.IntegerField()),
                ('parol', models.IntegerField()),
            ],
        ),
    ]
