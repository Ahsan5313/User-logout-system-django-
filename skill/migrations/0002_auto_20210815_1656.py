# Generated by Django 3.2.5 on 2021-08-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=50)),
                ('cemail', models.EmailField(blank=True, max_length=50)),
                ('cquery', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='myskill',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]