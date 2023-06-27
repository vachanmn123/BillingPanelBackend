from django import forms
from .models import Bill
import datetime


class BillForm(forms.ModelForm):
    def clean(self):
        if (
            self.cleaned_data["due_date"] < datetime.date.today()
            and not self.cleaned_data["is_paid"]
        ):
            raise forms.ValidationError("Due date cannot be in the past.")
