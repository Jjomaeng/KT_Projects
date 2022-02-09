# Generated by Django 4.0.1 on 2022-01-24 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50, null=True)),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PostTable',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=50)),
                ('post_image', models.ImageField(upload_to='')),
                ('post_contents', models.TextField(max_length=1000)),
                ('post_like', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myinfo.usertable')),
            ],
        ),
    ]