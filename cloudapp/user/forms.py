from django import forms


class UserForm(forms.Form):
    mail = forms.CharField(label='mail', max_length=254)