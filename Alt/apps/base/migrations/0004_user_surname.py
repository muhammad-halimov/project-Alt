# Generated by Django 5.0 on 2024-04-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_user_patronymic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
