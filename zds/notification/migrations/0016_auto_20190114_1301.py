# Generated by Django 2.1.5 on 2019-01-14 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0015_python_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='last_notification',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_notification', to='notification.Notification'),
        ),
    ]
