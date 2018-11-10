from django import forms

class ReservaForm(forms.Form):

	name = forms.CharField(label='Ingrese su nombre', max_length=100, required=True)
	total = forms.IntegerField(min_value=0, required=True)
	propertyId = forms.IntegerField(min_value=0, required=True)
	checkboxes = forms.MultipleChoiceField()
		
