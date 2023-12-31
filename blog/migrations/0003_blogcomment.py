# Generated by Django 4.2.6 on 2023-11-07 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_rename_s_no_post_sno_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
