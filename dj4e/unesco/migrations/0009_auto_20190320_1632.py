# Generated by Django 2.1.5 on 2019-03-20 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0008_auto_20190320_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iso',
            old_name='iso',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='region',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='states',
            old_name='state',
            new_name='name',
        ),
    ]