# Generated by Django 2.1.11 on 2019-11-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialv2', '0023_publishablecontent_validation_private_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishablecontent',
            name='beta_update_message_allowed',
            field=models.BooleanField(default=True, verbose_name='Si un message automatique doit être écrit à chaque mise à jour de la bêta'),
        ),
    ]
