# Generated by Django 3.2.7 on 2021-09-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='em_estoque',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
