# Generated by Django 2.0.2 on 2018-03-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='username',
        ),
        migrations.AddField(
            model_name='product',
            name='pname',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=1000000),
        ),
    ]