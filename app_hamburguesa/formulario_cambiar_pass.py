from django import forms

class cambiarPassForm(forms.Form):
    pass_vieja=forms.CharField(max_length=100,required=True)
    pass_nueva= forms.CharField(max_length=100,required=True)
    rep_pass=forms.CharField(max_length=100,required=True)
