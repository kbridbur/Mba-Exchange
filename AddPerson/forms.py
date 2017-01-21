from django import forms
from AddPerson.models import Client, Consultant, Editor, Provider, AddmissionsList, AddmissionsEntry
import mbaexchange.multiforms as mult


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

class AddmissionsListForm(forms.ModelForm):
    class Meta:
        model = AddmissionsList
        fields = '__all__'

class AddmissionsEntryForm(forms.ModelForm):
    class Meta:
        model = AddmissionsEntry
        fields = '__all__'

class AddmissionsPackageForm(mult.BaseMultipleFormsView):
    template_name = 'addmissions_packages_template.html'
    form_classes = {'container': AddmissionsListForm,
                 'entries': AddmissionsEntryForm}
    success_url = 'Add/'
