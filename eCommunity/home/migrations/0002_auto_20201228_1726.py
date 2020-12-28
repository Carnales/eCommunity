# Generated by Django 3.1.4 on 2020-12-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='name',
            new_name='store_name',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='category_slug',
        ),
        migrations.AddField(
            model_name='shop',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]