# Generated by Django 2.0.2 on 2018-03-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spend', models.CharField(max_length=200)),
                ('spend_amt', models.FloatField()),
                ('spend_date', models.DateTimeField(db_index=True)),
                ('spend_type', models.CharField(choices=[('SHP', 'Shoping'), ('PRT', 'Party'), ('DNT', 'Dine-out')], max_length=3)),
            ],
        ),
    ]
