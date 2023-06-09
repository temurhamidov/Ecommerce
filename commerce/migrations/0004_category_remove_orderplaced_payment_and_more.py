# Generated by Django 4.2.1 on 2023-05-09 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_payment_orderplaced'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce.category'),
        ),
    ]
