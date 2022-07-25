# Generated by Django 4.0.6 on 2022-07-25 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('photo', models.ImageField(upload_to='pictures/%Y_%m/')),
                ('category', models.CharField(choices=[('funny', 'Funny :>'), ('serious', 'Serious cat :|'), ('cute', 'Very cute OwO')], default='funny', max_length=7)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_edited', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
    ]
