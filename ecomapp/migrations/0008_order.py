# Generated by Django 2.2 on 2019-05-05 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecomapp', '0007_auto_20190505_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('firs_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('buying_type', models.CharField(choices=[('Самовивіз', 'Самовивіз'), ('Доставка', 'Доставка')], max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(max_length=500)),
                ('status', models.CharField(choices=[('Прийнятий в обробку', 'Прийнятий в обробку'), ('Виконується', 'Виконується'), ('Оплачено', 'Оплачено')], max_length=100)),
                ('items', models.ManyToManyField(to='ecomapp.Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
