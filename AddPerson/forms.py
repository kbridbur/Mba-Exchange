from django import forms
from AddPerson.models import Client, Consultant, Editor, Provider, AddmissionsService, Service, School
import mbaexchange.multiforms as mult
import AddPerson.enumerations as enums


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

    client = forms.ModelChoiceField(queryset = Client.objects.all(), required = False)
    consultant = forms.ModelChoiceField(queryset = Consultant.objects.all(), required = False)
    schools = forms.ModelMultipleChoiceField(queryset = School.objects.all(), required = False)
    addmissions_service = forms.ChoiceField(choices=enums.POSSIBLE_ADMISSIONS_SERVICES, required = False)

    class Meta:
        model = AddmissionsService
        fields = '__all__'

class ServiceForm(forms.ModelForm):

    client = forms.ModelChoiceField(queryset = Client.objects.all(), required = False)
    provider = forms.ModelChoiceField(queryset = Provider.objects.all(), required = False)
    service = forms.ChoiceField(choices=enums.POSSIBLE_SERVICES, required = False)

    class Meta:
        model = Service
        fields = '__all__'
