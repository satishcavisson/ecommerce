# Generated by Django 2.1.4 on 2019-07-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_bg', models.ImageField(upload_to='pics')),
                ('banner_collection_type', models.CharField(max_length=50)),
                ('banner_caption', models.CharField(max_length=50)),
            ],
        ),
    ]
