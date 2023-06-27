from django.contrib import admin
from .models import Customer, Bill, Transaction, BillItem, Item
from .forms import BillForm

# Register your models here.


@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):
    list_display = ("bill", "item", "quantity")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")


@admin.register(Customer)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("user",)


class BillItemInline(admin.TabularInline):
    model = BillItem
    extra = 0


@admin.register(Bill)
class RegisterAdmin(admin.ModelAdmin):
    form = BillForm
    list_display = (
        "customer",
        "amount",
        "currency",
        "date_of_generation",
        "due_date",
        "is_paid",
        "items",
    )
    inlines = [BillItemInline]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "bill",
        "amount",
    )
