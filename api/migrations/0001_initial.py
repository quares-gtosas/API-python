# Generated by Django 5.0.6 on 2024-05-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskid', models.IntegerField()),
                ('task_desc', models.CharField(max_length=2000)),
                ('task_title', models.CharField(max_length=200)),
                ('estimation_hour', models.IntegerField()),
                ('owner_id', models.IntegerField()),
            ],
        ),
    ]
