# Generated by Django 5.0.1 on 2024-02-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='user_ID',
            field=models.CharField(max_length=255),
        ),
    ]
