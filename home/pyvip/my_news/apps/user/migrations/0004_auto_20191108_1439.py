# Generated by Django 2.1.7 on 2019-11-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.RemoveField(
            model_name='users',
            name='email_ac',
        ),
        migrations.RemoveField(
            model_name='users',
            name='identifier',
        ),
        migrations.AddField(
            model_name='users',
            name='email_active',
            field=models.BooleanField(default=False, verbose_name='邮箱验证状态'),
        ),
    ]