# Generated by Django 3.1.2 on 2020-11-11 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webrtcroomId', models.CharField(max_length=200)),
                ('is_view', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='accounts.client')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='api.program')),
            ],
        ),
    ]
