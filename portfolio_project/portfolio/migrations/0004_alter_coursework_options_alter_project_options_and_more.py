# Generated by Django 5.1.1 on 2024-10-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_skill_options_skill_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursework',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order']},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='link',
            new_name='url',
        ),
        migrations.AddField(
            model_name='coursework',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coursework',
            name='course_name',
            field=models.CharField(max_length=200),
        ),
    ]
