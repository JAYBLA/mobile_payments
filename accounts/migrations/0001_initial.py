# Generated by Django 2.2.23 on 2021-05-31 06:52

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Email Address')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_tutor', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_picture', models.ImageField(default='default.png', upload_to=accounts.models.profile_pic_filename)),
                ('website', models.URLField(blank=True)),
                ('country', django_countries.fields.CountryField(default='TZ', max_length=2, verbose_name='Country')),
                ('location', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True)),
                ('youtube_link', models.URLField(blank=True, null=True, verbose_name='Youtube URL')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='Facebook URL')),
                ('instagram_link', models.URLField(blank=True, null=True, verbose_name='Instagram URL')),
                ('linkedin_link', models.URLField(blank=True, null=True, verbose_name='Linkedin URL')),
                ('twitter_link', models.URLField(blank=True, null=True, verbose_name='Twitter URL')),
                ('github_link', models.URLField(blank=True, null=True, verbose_name='Github URL')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
