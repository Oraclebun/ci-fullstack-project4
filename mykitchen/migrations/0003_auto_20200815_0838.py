# Generated by Django 2.2.14 on 2020-08-15 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mykitchen.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mykitchen', '0002_auto_20200814_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kitchen Fixtures', max_length=50)),
                ('storage_temperature', models.IntegerField(blank=True)),
                ('editted_by', models.ForeignKey(on_delete=models.SET(mykitchen.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='household',
            name='member',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mykitchen.StorageLocation'),
        ),
        migrations.AlterField(
            model_name='household',
            name='owner',
            field=models.ForeignKey(on_delete=models.SET(mykitchen.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='storagelocation',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mykitchen.Household'),
        ),
        migrations.AddField(
            model_name='member',
            name='household',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='household', to='mykitchen.Household'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
