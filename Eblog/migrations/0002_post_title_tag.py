# Generated by Django 2.2.4 on 2021-03-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='VectorBlog', max_length=200),
        ),
    ]