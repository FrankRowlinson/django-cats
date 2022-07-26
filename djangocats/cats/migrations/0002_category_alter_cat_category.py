# Generated by Django 4.0.6 on 2022-08-01 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='cat',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cats.category'),
        ),
    ]
