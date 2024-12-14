# Generated by Django 5.1.4 on 2024-12-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_rename_title_game_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='age_limited',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(to='task1.buyer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]