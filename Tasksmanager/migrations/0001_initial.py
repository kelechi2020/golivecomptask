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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_elasped_dev', models.IntegerField(verbose_name='Time Elasped', default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('client_name', models.CharField(max_length=1000, verbose_name='Client Name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('time_elasped', models.IntegerField(verbose_name='Elapsed Time', default=None, null=True, blank=True)),
                ('importance', models.IntegerField(verbose_name='Importance')),
                ('project', models.ForeignKey(to='Tasksmanager.Project', null=True, verbose_name='Project', default=None, blank=True)),
            ],
            options={
                'verbose_name_plural': 'tasks',
                'verbose_name': 'task',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_auth', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('login', models.CharField(max_length=25, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone Number', default=None, null=True, blank=True)),
                ('born_date', models.DateField(verbose_name='Born Date', default=None, null=True, blank=True)),
                ('last_connection', models.DateTimeField(verbose_name='Date Of Last Connection', default=None, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('years_seniority', models.IntegerField(verbose_name='Seniority', default=0)),
                ('date_created', models.DateTimeField(verbose_name='Date Of birthday', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(serialize=False, auto_created=True, to='Tasksmanager.UserProfile', parent_link=True, primary_key=True)),
            ],
            bases=('Tasksmanager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(serialize=False, auto_created=True, to='Tasksmanager.UserProfile', parent_link=True, primary_key=True)),
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
