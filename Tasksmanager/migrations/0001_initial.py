# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperWorkTask',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('time_elasped_dev', models.IntegerField(null=True, blank=True, verbose_name='Time Elasped', default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, verbose_name='modification date and time', null=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('client_name', models.CharField(max_length=1000, verbose_name='Client Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('time_elasped', models.IntegerField(null=True, blank=True, verbose_name='Elapsed Time', default=None)),
                ('importance', models.IntegerField(verbose_name='Importance')),
                ('project', models.ForeignKey(blank=True, default=None, to='Tasksmanager.Project', null=True, verbose_name='Project')),
            ],
            options={
                'verbose_name_plural': 'tasks',
                'verbose_name': 'task',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_auth', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('login', models.CharField(max_length=25, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('phone', models.CharField(max_length=20, null=True, blank=True, verbose_name='Phone Number', default=None)),
                ('born_date', models.DateField(null=True, blank=True, verbose_name='Born Date', default=None)),
                ('last_connection', models.DateTimeField(null=True, blank=True, verbose_name='Date Of Last Connection', default=None)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('years_seniority', models.IntegerField(verbose_name='Seniority', default=0)),
                ('date_created', models.DateTimeField(verbose_name='Date Of birthday', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='Tasksmanager.UserProfile')),
            ],
            bases=('Tasksmanager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, primary_key=True, to='Tasksmanager.UserProfile')),
                ('specialization', models.CharField(max_length=50, verbose_name='Specialization')),
            ],
            bases=('Tasksmanager.userprofile',),
        ),
        migrations.AddField(
            model_name='developerworktask',
            name='task',
            field=models.ForeignKey(to='Tasksmanager.Task', verbose_name='Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='developers',
            field=models.ManyToManyField(related_name='dev1', to='Tasksmanager.Developer', verbose_name='Second Developer'),
        ),
        migrations.AddField(
            model_name='developerworktask',
            name='developer',
            field=models.ForeignKey(to='Tasksmanager.Developer', verbose_name='Developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(to='Tasksmanager.Supervisor', verbose_name='Supervisor'),
        ),
    ]
