from django import forms
class compny_form(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    age=forms.IntegerField()
    bart=forms.DateField(required=False)

