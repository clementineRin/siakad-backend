# Generated by Django 4.1.7 on 2023-03-08 02:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0021_jadwalmakul'),
    ]

    operations = [
        migrations.CreateModel(
            name='KHS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('program_studi', models.CharField(max_length=255)),
                ('program_pendidikan', models.CharField(max_length=255)),
                ('tahun_akademik_awal', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(3000)])),
                ('tahun_akademik_akhir', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(3000)])),
                ('dosen_pembimbing', models.CharField(max_length=255)),
                ('kelas', models.CharField(max_length=5)),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='khs_list', to='academic.mahasiswa')),
            ],
        ),
    ]
