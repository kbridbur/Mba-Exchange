from django import forms
from AddPerson.models import *

class AddClientForm(forms.Form):

    client_first_name = forms.CharField(label = "Client first name", max_length = 50)
    client_last_name = forms.CharField(label = "Client last name", max_length = 50)
    new_client = Client.CreateClient(Client, client_first_name, client_last_name)
    new_client.save()
