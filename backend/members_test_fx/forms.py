from django import forms

from members_test_fx.models import Games

class FormTest(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    surname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField(required=True)

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'

