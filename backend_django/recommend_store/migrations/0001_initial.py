# Generated by Django 3.1.1 on 2020-09-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compatibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_a', models.CharField(db_column='FOOD_A', max_length=45)),
                ('food_b', models.CharField(db_column='FOOD_B', max_length=45)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=100, null=True)),
                ('search_cnt', models.IntegerField(db_column='SEARCH_CNT')),
                ('avg_star', models.FloatField(db_column='AVG_STAR')),
                ('review_cnt', models.IntegerField(db_column='REVIEW_CNT')),
            ],
            options={
                'db_table': 'COMPATIBILITY',
                'managed': False,
            },
        ),
    ]
