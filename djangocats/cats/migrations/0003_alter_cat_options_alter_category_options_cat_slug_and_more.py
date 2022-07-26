# Generated by Django 4.0.6 on 2022-08-14 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_category_alter_cat_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cat',
            options={'ordering': ['-time_created']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='cat',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cat',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
