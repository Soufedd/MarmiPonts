from django import forms
from Core.models import Information, Ingredient



class InformationForm(forms.ModelForm):
	class Meta:
		model = Information
		exclude = ('user',)


class SearchField(forms.Form):
	search_recipe = forms.CharField(max_length=60, required=False)

class IngredientField(forms.ModelForm):
	class Meta:
		model= Ingredient
		exclude = ('user',)

