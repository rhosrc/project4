# Generated by Django 4.0.3 on 2022-03-19 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_memo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memo',
            options={'ordering': ('-date', 'title')},
        ),
    ]
