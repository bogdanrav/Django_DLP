# Generated by Django 4.0.2 on 2022-02-22 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regular_Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Regular Description')),
                ('expression', models.CharField(max_length=250, verbose_name='Expression')),
            ],
            options={
                'db_table': 'regular_expression',
            },
        ),
        migrations.CreateModel(
            name='Detected_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('regression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slack_events_test.regular_expression')),
            ],
            options={
                'db_table': 'detected_message',
            },
        ),
    ]
