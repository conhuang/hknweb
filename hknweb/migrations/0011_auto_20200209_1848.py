# Generated by Django 2.1.11 on 2020-02-10 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hknweb', '0010_homeannouncement'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeAnnouncement',
            new_name='Announcement',
        ),
    ]