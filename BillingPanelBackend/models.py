from typing import Iterable, Optional
from django.db import models
import datetime


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"


class BillItem(models.Model):
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ("bill", "item")

    def save(self, *args) -> None:
        super().save(*args)
        self.bill.updateTotal()
        return None

    def __str__(self) -> str:
        return f"{self.bill.pk} - {self.item.name}"


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    date_of_generation = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=None, null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} - {self.customer.user.username}"

    def items(self) -> list[BillItem]:
        return [item for item in self.billitem_set.all()]

    def updateTotal(self) -> None:
        self.amount = sum(
            [item.item.price * item.quantity for item in self.billitem_set.all()]
        )
        self.save()

    def save(
        self,
        *args,
    ) -> None:
        return super().save(*args)


class Transaction(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # TODO: Add fields from the gateway.

    def __str__(self) -> str:
        return f"{self.bill.customer.user.username}-{self.pk}"
