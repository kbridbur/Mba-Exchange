from django import forms
from AddPerson.models import Client, Consultant, Editor, Provider, AddmissionsService, Service
import mbaexchange.multiforms as mult


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        exclude = ['clients']

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = '__all__'

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = ['clients']

class AddmissionsServiceForm(forms.ModelForm):
    class Meta:
        model = AddmissionsService
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
