from django import forms
from AddPerson.models import Client, Consultant, Editor, Provider

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = '__all__'

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = '__all__'

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
