# Generated by Django 3.0.4 on 2020-03-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mob', models.BigIntegerField()),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
    ]
