# Generated by Django 4.2.3 on 2023-07-20 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_count_views_blog_sign_of_publication_blog_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Content',
            new_name='content',
        ),
    ]
