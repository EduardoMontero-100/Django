# Generated by Django 4.0 on 2022-07-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_entrega', models.CharField(max_length=50)),
                ('tipo_entrega', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateField()),
            ],
        ),
    ]
