# Generated by Django 2.2.28 on 2024-02-04 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20240204_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
