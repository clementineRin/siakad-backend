# Generated by Django 4.1.7 on 2023-03-14 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academic', '0036_alter_programstudi_no_sk_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempStaffProdi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_induk', models.CharField(max_length=20, unique=True)),
                ('no_hp', models.CharField(max_length=255)),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.programstudi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
