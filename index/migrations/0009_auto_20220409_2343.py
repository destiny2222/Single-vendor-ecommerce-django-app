# Generated by Django 2.2 on 2022-04-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
