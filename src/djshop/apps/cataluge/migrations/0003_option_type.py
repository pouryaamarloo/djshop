# Generated by Django 4.2.4 on 2025-03-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cataluge', '0002_productclass_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('float', 'Float'), ('option', 'Option'), ('multi_option', 'Multi Option')], default='text', max_length=100),
        ),
    ]
