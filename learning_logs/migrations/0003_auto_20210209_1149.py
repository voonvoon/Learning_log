# Generated by Django 3.1.6 on 2021-02-09 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.topic'),
        ),
    ]
