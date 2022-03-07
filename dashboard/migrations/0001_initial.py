# Generated by Django 3.2.5 on 2022-03-02 06:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('discription', models.TextField()),
                ('tasks', models.TextField()),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_user', to=settings.AUTH_USER_MODEL, verbose_name='author of project')),
                ('members', models.ManyToManyField(related_name='pmembers', to=settings.AUTH_USER_MODEL, verbose_name='members of project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.FileField(upload_to='')),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='dashboard.project')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('msg', models.TextField()),
                ('msgTime', models.DateTimeField(default=datetime.datetime.now)),
                ('mfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mfrom', to=settings.AUTH_USER_MODEL)),
                ('mto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]