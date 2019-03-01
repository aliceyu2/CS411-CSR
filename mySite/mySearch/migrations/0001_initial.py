# Generated by Django 2.1.7 on 2019-03-01 05:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('completionDate', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='serviceRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestNumber', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.AddField(
            model_name='csr',
            name='requestNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mySearch.serviceRequest'),
        ),
    ]
