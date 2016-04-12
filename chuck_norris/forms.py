from django import forms
 
class PostForm(forms.Form):
	voornaam = forms.CharField(max_length=256)
	achternaam = forms.CharField(max_length=256)
	fields = ['voornaam', 'achtenraam']
