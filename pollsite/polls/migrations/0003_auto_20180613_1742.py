# Generated by Django 2.0.6 on 2018-06-13 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='answer',
            new_name='question',
        ),
    ]
