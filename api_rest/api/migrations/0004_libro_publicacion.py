# Generated by Django 3.2.3 on 2021-07-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_libro_sinopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='publicacion',
            field=models.DateField(null=True),
        ),
    ]