from django import forms
from .models import ModelWithCSV


class ModelWithCSVForm(forms.ModelForm):
    class Meta:
        model = ModelWithCSV
        fields = '__all__'

    def clean_csv_field(self):
        data = self.data.getlist('csv_field')
        return data
