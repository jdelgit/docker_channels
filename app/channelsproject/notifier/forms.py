from django import forms
from .models import DummyModel

class SampleForm(forms.ModelForm):

    class Meta:
        model = DummyModel
        fields = "__all__"
