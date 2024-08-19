# Generated by Django 5.0.6 on 2024-08-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_clients_username_serves_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serves',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='serves',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='serves',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]