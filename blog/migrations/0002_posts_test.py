# Generated by Django 2.2.5 on 2019-10-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('link', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('publish', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
