# Generated by Django 3.2 on 2021-05-18 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='id',
        ),
        migrations.AlterField(
            model_name='service',
            name='hospital',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.hospital'),
        ),
        migrations.AlterField(
            model_name='service',
            name='oxygen_beds_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='oxygen_beds_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='oxygen_cylinder_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='oxygen_cylinder_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='ventilator_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='ventilator_total',
            field=models.IntegerField(default=0),
        ),
    ]
