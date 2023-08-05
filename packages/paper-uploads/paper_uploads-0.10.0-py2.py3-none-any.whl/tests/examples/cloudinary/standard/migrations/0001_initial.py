# Generated by Django 4.0.1 on 2022-02-14 06:28

from django.db import migrations, models
import django.db.models.deletion
import paper_uploads.cloudinary.models.fields.file
import paper_uploads.cloudinary.models.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paper_uploads_cloudinary', '0005_auto_20211116_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', paper_uploads.cloudinary.models.fields.file.CloudinaryFileField(blank=True, on_delete=django.db.models.deletion.SET_NULL, storage=None, to='paper_uploads_cloudinary.cloudinaryfile', upload_to='', verbose_name='file')),
                ('image', paper_uploads.cloudinary.models.fields.image.CloudinaryImageField(blank=True, on_delete=django.db.models.deletion.SET_NULL, storage=None, to='paper_uploads_cloudinary.cloudinaryimage', upload_to='', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Page',
            },
        ),
    ]
