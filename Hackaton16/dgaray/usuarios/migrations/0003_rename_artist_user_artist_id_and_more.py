# Generated by Django 4.2.2 on 2023-06-23 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0002_alter_user_artist_alter_user_playlist"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="artist",
            new_name="artist_id",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="playlist",
            new_name="playlist_id",
        ),
    ]
