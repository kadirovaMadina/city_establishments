# Generated by Django 4.2.4 on 2023-08-12 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_name', models.CharField(max_length=50, verbose_name='Название заведения')),
                ('description', models.TextField(verbose_name='Описание заведения')),
                ('address', models.CharField(max_length=30, verbose_name='Адрес заведения(улица и номер)')),
                ('city', models.CharField(max_length=25, verbose_name='Город')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='establishments', to='categories.category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='establishments', to='categories.type')),
            ],
            options={
                'verbose_name': 'Заведение',
                'verbose_name_plural': 'Заведения',
            },
        ),
    ]
