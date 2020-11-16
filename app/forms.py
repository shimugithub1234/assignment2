from django import forms


class Number(forms.Form):
    num = forms.IntegerField(label="Enter a Number")