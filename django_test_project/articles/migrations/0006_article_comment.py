# Generated by Django 4.0.3 on 2022-04-19 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.article_comment'),
        ),
    ]
