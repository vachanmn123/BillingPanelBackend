# Generated by Django 4.2.2 on 2023-06-27 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BillingPanelBackend', '0002_item_alter_bill_due_date_billitem'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='billitem',
            unique_together={('bill', 'item')},
        ),
    ]