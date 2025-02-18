# Generated by Django 5.0.6 on 2024-06-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_alter_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
