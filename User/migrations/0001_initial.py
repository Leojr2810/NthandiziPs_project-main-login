# Generated by Django 4.1.5 on 2023-05-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('pnumber', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('otp', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
