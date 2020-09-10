# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-06-18 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "challenges",
            "0065_add_cluster_details_to_challenge_evaluation_cluster_model",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="challengephase",
            name="is_partial_submission_evaluation_enabled",
            field=models.BooleanField(default=False),
        ),
    ]
