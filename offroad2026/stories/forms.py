from django import forms
from offroad2026.stories.models import Story


class StoryCreateForm(forms.ModelForm):

    class Meta:
        model = Story

        exclude = ["created_at"]

        labels = {
            "title": "Story Title",
            "content": "Story Content",
            "destination": "Destination",
            "vehicles": "Vehicles Used",
            "trip_date": "Trip Date",
        }

        help_texts = {
            "vehicles": "Select vehicles used during the trip."
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Epic mountain climb"
            }),
            "content": forms.Textarea(attrs={
                "placeholder": "Describe your offroad adventure..."
            }),
            "trip_date": forms.DateInput(attrs={
                "type": "date"
            }),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]

        if "test" in title.lower():
            raise forms.ValidationError(
                "Title cannot contain the word 'test'."
            )

        return title


class StoryDeleteForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True