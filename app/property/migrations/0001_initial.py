# Generated by Django 4.2.1 on 2023-09-19 21:18

import app.service.service
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, choices=[('no', 'no'), ('CHUI', 'CHUI'), ('DJALAL-ABAD', 'DJALAL-ABAD'), ('OSH', 'OSH'), ('NARYN', 'NARYN'), ('TALAS', 'TALAS'), ('ISSYK-KUL', 'ISSYK-KUL')], max_length=300, verbose_name='region')),
                ('street', models.CharField(max_length=50, verbose_name='street')),
                ('apartment', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storey', models.CharField(blank=True, choices=[('Bungalow', 'Bungalow'), ('Duplex', 'Duplex'), ('One Storeys', 'One Storeys'), ('Two Storeys', 'Two Storeys'), ('Three Storeys', 'Three Storeys'), ('Four Storeys', 'Four Storeys'), ('Five Storeys', 'Five Storeys')], max_length=300, verbose_name='storey')),
                ('bedroom', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=300, unique=True, verbose_name='bed')),
                ('bathroom', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=300, verbose_name='bathroom')),
                ('furnished', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no'), ('somewhat', 'somewhat')], max_length=300, verbose_name='furnished')),
                ('parking_space', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=300, verbose_name='parking_space')),
                ('new_property', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=300, verbose_name='new_property')),
                ('purpose', models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Office', 'Office'), ('Business', 'Business'), ('Other', 'Other')], max_length=300, unique=True, verbose_name='purpose')),
                ('square_meter', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20)),
                ('slug', models.SlugField(max_length=100)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='property.address', verbose_name='Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to=app.service.service.upload_image_path)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.property')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='property.feedback')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_choices', models.CharField(choices=[('rent', 'Rent'), ('sale', 'Sale'), ('term', 'Term')], max_length=10, verbose_name='deal')),
                ('currency_choices', models.CharField(choices=[('no', 'no'), ('ru', 'RU'), ('us', 'US'), ('som', 'SOM'), ('EU', 'EU')], max_length=10, verbose_name='currency')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('additional_info', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('duration', models.CharField(blank=True, choices=[('1 month', '1 month'), ('3 months', '3 months'), ('6 months', '6 months'), ('Year', 'Year'), ('2 Years', '2 Years'), ('3 Years', '3 Years')], max_length=300, verbose_name='duration')),
                ('feedback', models.ManyToManyField(blank=True, default=None, to='property.feedback')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_advertisement', to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishlist', models.ManyToManyField(blank=True, default=None, related_name='wishlist_advertisement', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='property.city', verbose_name='City'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='property.district', verbose_name='District'),
        ),
    ]
