# Generated by Django 5.0.3 on 2024-03-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=136)),
                ('company', models.CharField(max_length=36)),
                ('color', models.CharField(max_length=64)),
                ('RAM', models.CharField(max_length=36)),
                ('memory', models.CharField(max_length=48)),
                ('price', models.FloatField()),
                ('img_url', models.CharField(max_length=144)),
            ],
        ),
        migrations.DeleteModel(
            name='Talaba',
        ),
    ]
