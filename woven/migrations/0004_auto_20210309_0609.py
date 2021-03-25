# Generated by Django 3.1.7 on 2021-03-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woven', '0003_merge_20210301_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='MandateId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandate_id', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='apirequest',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]