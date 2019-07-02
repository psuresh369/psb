# Generated by Django 2.2.2 on 2019-06-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('completed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
            ],
            options={
                'db_table': 'create',
            },
        ),
    ]
