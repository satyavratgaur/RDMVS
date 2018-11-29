# Generated by Django 2.1.3 on 2018-11-27 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(help_text='User name', max_length=50)),
                ('psw', models.CharField(help_text='Password', max_length=50)),
            ],
            options={
                'ordering': ['-uname', '-psw'],
            },
        ),
    ]