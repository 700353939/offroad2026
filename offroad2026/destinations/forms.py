from django import forms
from offroad2026.destinations.models import Destination


class DestinationBaseForm(forms.ModelForm):

    class Meta:
        model = Destination
        fields = "__all__"

        labels = {
            "name": "Destination Name",
            "location": "Location",
            "difficulty": "Difficulty Level",
            "description": "Description",
            "image_url": "Image URL",
        }

        help_texts = {
            "name": "Enter the name of the offroad location.",
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Rhodope Mountains trail"
            }),
            "location": forms.TextInput(attrs={
                "placeholder": "Bulgaria"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Describe the terrain and route..."
            }),
        }


class DestinationCreateForm(DestinationBaseForm):
    pass


class DestinationEditForm(DestinationBaseForm):
    pass


class DestinationDeleteForm(DestinationBaseForm):

    class Meta(DestinationBaseForm.Meta):
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True