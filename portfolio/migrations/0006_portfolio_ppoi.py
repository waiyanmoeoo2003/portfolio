# Generated by Django 5.0 on 2024-01-09 16:31

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_rename_linked_in_portfolio_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(blank=True, default='0.5x0.5', editable=False, max_length=20, null=True),
        ),
    ]
