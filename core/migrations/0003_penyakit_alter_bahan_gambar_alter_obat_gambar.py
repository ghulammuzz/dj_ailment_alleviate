# Generated by Django 4.1.7 on 2023-02-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_obat_delete_penyakit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penyakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_penyakit', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='penyakit/')),
            ],
        ),
        migrations.AlterField(
            model_name='bahan',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='bahan/'),
        ),
        migrations.AlterField(
            model_name='obat',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='obat/'),
        ),
    ]
