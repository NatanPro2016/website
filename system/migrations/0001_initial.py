# Generated by Django 4.2.4 on 2023-08-23 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HomeMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField(max_length=20)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20)),
                ('campaus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('WE', 'weekend'), ('RE', 'regular'), ('EX', 'extension')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('middle_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('sex', models.CharField(blank=True, max_length=10)),
                ('phone_no', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Studet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('middle_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('sex', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=40)),
                ('status', models.CharField(blank=True, choices=[('PE', 'pending'), ('ST', 'started')], default='pending', max_length=40)),
                ('type', models.CharField(choices=[('WE', 'weekend'), ('RE', 'regular'), ('EX', 'extension')], max_length=50)),
                ('sector', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='system.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=50)),
                ('time', models.CharField(choices=[('MO', 'Morning'), ('AF', 'Afternoon'), ('NI', 'Night')], max_length=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.room')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.sector')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.teacher')),
            ],
        ),
    ]
