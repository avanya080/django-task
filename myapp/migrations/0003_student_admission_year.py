# Generated by Django 2.0.3 on 2019-05-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_student_admission_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_year',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
    ]