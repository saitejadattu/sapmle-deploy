# Generated by Django 5.2.3 on 2025-06-27 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
