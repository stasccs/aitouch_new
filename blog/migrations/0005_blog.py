# Generated by Django 2.2.5 on 2019-10-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191006_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('annotation', models.CharField(max_length=400)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to='media')),
                ('publish', models.DateTimeField()),
            ],
        ),
    ]