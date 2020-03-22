# Generated by Django 3.0.4 on 2020-03-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(blank=True, max_length=1024, verbose_name='摘要'),
        ),
    ]