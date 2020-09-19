from django import forms


class NameForm(forms.Form):
    login = forms.CharField(label='Login', max_length=100)

    # password = forms.CharField(label='Hasło', max_length=100)
