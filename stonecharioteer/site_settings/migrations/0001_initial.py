# Generated by Django 2.0.13 on 2019-09-14 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True, help_text='Twitter URL', null=True)),
                ('github', models.URLField(blank=True, help_text='Github URL', null=True)),
                ('gitlab', models.URLField(blank=True, help_text='Gitlab URL', null=True)),
                ('youtube', models.URLField(blank=True, help_text='Youtube URL', null=True)),
                ('pypi', models.URLField(blank=True, help_text='PyPI URL', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
