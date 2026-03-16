from django import forms
from offroad2026.vehicles.models import Vehicle


class VehicleBaseForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        exclude = []

        labels = {
            "brand": "Brand",
            "model": "Model",
            "year": "Production Year",
            "engine": "Engine Type",
            "horsepower": "Horsepower",
            "description": "Description",
            "image_url": "Image URL",
        }

        widgets = {
            "brand": forms.TextInput(attrs={
                "placeholder": "Toyota"
            }),
            "model": forms.TextInput(attrs={
                "placeholder": "C-HR"
            }),
            "year": forms.NumberInput(attrs={
                "placeholder": "2020"
            }),
        }


class VehicleCreateForm(VehicleBaseForm):
    pass


class VehicleEditForm(VehicleBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["year"].disabled = True