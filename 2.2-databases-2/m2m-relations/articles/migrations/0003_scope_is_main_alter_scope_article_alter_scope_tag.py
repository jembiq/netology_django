# Generated by Django 4.1.1 on 2022-09-26 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_tag_scope_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
    ]
