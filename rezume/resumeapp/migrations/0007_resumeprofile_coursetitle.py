# Generated by Django 4.2.14 on 2024-08-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0006_rename_addinfo_resumeprofile_degreecertification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeprofile',
            name='coursetitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
