# Generated by Django 3.1.2 on 2020-11-10 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0003_auto_20201110_0212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treecategory',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelTable(
            name='treecategory',
            table='category',
        ),
    ]
