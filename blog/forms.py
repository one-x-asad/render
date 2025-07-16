from django import forms
import re
from django.core.exceptions import ValidationError

class UserDataForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise ValidationError("Parol Xato")
        if not re.search(r'[A-Za-z]', password):
            raise ValidationError("Parol Xato")
        if not re.search(r'[0-9]', password):
            raise ValidationError("Parol Xato")
        return password


