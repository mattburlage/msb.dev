# Generated by Django 2.2.8 on 2020-03-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msbdev', '0005_contactform_added_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
