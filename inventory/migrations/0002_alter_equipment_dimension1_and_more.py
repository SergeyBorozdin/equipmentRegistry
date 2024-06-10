# Generated by Django 5.0.6 on 2024-06-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='dimension1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='dimension2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='dimension3',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='equipment_photos/'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='storage_location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='supplier_art',
            field=models.CharField(default=0.0, max_length=200),
            preserve_default=False,
        ),
    ]
