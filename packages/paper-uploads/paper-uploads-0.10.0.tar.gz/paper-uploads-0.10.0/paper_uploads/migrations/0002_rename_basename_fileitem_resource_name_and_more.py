# Generated by Django 4.0.1 on 2022-02-16 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper_uploads', '0001_squashed_0009_alter_collectionitembase_polymorphic_ctype_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileitem',
            old_name='basename',
            new_name='resource_name',
        ),
        migrations.RenameField(
            model_name='imageitem',
            old_name='basename',
            new_name='resource_name',
        ),
        migrations.RenameField(
            model_name='svgitem',
            old_name='basename',
            new_name='resource_name',
        ),
        migrations.RenameField(
            model_name='uploadedfile',
            old_name='basename',
            new_name='resource_name',
        ),
        migrations.RenameField(
            model_name='uploadedimage',
            old_name='basename',
            new_name='resource_name',
        ),
    ]
