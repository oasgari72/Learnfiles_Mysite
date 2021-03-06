# Generated by Django 3.0.4 on 2020-03-10 14:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200310_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.Title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=datetime.datetime(2020, 3, 10, 14, 39, 13, 86353, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
