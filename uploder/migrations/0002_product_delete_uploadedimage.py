# Generated by Django 5.0.6 on 2024-12-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('newprice', models.IntegerField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedImage',
        ),
    ]
