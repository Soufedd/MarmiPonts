from django import forms
from Core.models import Information



class InformationForm(forms.ModelForm):
	class Meta:
		model = Information
		exclude = ('user',)


# class SearchField(forms.Form):
# 	search_recipe = forms.CharField(required=False)

class SearchField(forms.Form):
	search_recipe = forms.CharField(max_length=60, required=False)


