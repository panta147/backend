# Generated by Django 4.1.3 on 2022-12-06 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_myuser_companyname_alter_myuser_companytype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='image',
        ),
    ]
