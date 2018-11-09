from django import forms

class ReservaForm(forms.Form):

	name = forms.CharField(label='Ingrese su nombre', max_length=100, required=True)
	dateFrom = forms.DateField(label='Fecha Inicio', required=True)
	dateTo = forms.DateField(label='Fecha Fin', required=True)
	total = forms.IntegerField(min_value=0, required=True)
	propertyId = forms.IntegerField(min_value=0, required=True)