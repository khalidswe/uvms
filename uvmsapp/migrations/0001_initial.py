# Generated by Django 4.1.4 on 2022-12-14 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('student_id', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='app/img/student')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uvmsapp.usermaster')),
            ],
        ),
        migrations.CreateModel(
            name='Officials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('officials_id', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='app/img/officials')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uvmsapp.usermaster')),
            ],
        ),
    ]