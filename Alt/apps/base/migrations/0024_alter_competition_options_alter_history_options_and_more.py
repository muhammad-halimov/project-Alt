# Generated by Django 5.0 on 2024-04-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_history_competition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'ordering': ['-start_time'], 'verbose_name': 'Competition', 'verbose_name_plural': 'Competitions'},
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['-updated'], 'verbose_name': 'History', 'verbose_name_plural': 'History'},
        ),
        migrations.AddField(
            model_name='competition',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
    ]