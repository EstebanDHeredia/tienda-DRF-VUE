# Generated by Django 4.2.14 on 2024-07-12 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_category_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="get_products",
                to="products.category",
                verbose_name="Categoría",
            ),
            preserve_default=False,
        ),
    ]
