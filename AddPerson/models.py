from django.db import models
from datetime import datetime
import AddPerson.enumerations as enums

'''
Represents a consultants editor. conusltants may be their own editors in which case both objects will exist with the same name
Contains no information about who they edit
'''
class Editor(models.Model):
    payment = models.IntegerField(default = 0, blank = True, null = True)
    first_name = models.CharField(max_length = 100, blank = True, null = True)
    last_name = models.CharField(max_length = 100, blank = True, null = True)

    @staticmethod
    def FindEditorsByName(name):
        name_arr = name.split(" ") #split potential first and last name
        name_arr = [item for item in name_arr if item != ""] #remove empty strings
        if len(name_arr) == 0: #no name given, display everything
            return Editor.objects.order_by('first_name', 'last_name').all()
        elif len(name_arr) == 1: #just first name or last name
            by_first_name = Editor.objects.filter(first_name=name_arr[0]).order_by('first_name', 'last_name').all()
            by_last_name = Editor.objects.filter(last_name=name_arr[0]).order_by('first_name', 'last_name').all()
            if len(by_first_name) >= len(by_last_name):
                return by_first_name
            return by_last_name
        else: #first and last name
            return Editor.objects.filter(first_name=name_arr[0], last_name=name_arr[1]).order_by('first_name', 'last_name').all()

    def __str__(self):
        return self.first_name + " " + self.last_name

'''
Represents a consultant as an object containing all of their personal information.
Contains no information about relationship with clients or packages
'''
class Consultant(models.Model):
    payment = models.IntegerField(default = 0, blank = True, null = True)
    first_name = models.CharField(max_length = 100, blank = True, null = True)
    last_name = models.CharField(max_length = 100, blank = True, null = True)
    consultant_specialty = models.CharField(max_length = 50, choices=enums.SPECIALTIES, default = enums.SPECIALTIES[0][0], blank = True, null = True)
    consultant_address = models.CharField(max_length = 200, blank = True, null = True)
    editor = models.ForeignKey(Editor, blank = True, null = True)

    @staticmethod
    def FindConsultantsByName(name):
        name_arr = name.split(" ") #split potential first and last name
        name_arr = [item for item in name_arr if item != ""] #remove empty strings
        if len(name_arr) == 0: #no name given, display everything
            return Consultant.objects.order_by('first_name', 'last_name').all()
        elif len(name_arr) == 1: #just first name or last name
            by_first_name = Consultant.objects.filter(first_name=name_arr[0]).order_by('first_name', 'last_name').all()
            by_last_name = Consultant.objects.filter(last_name=name_arr[0]).order_by('first_name', 'last_name').all()
            if len(by_first_name) >= len(by_last_name):
                return by_first_name
            return by_last_name
        else: #first and last name
            return Consultant.objects.filter(first_name=name_arr[0], last_name=name_arr[1]).order_by('first_name', 'last_name').all()

    @staticmethod
    def GetClients(first_name, last_name):
        clients = set()
        for package in Consultant.objects.select_related(first_name = first_name, last_name = last_name).all():
            clients.add(package.container.client)
        return clients

    def CreateConsultant(cls, payment, first_name, last_name, specialty, address, editor):
        consultant = cls(payment = payment,
                    first_name = first_name,
                    last_name = last_name,
                    consultant_specialty = specialty,
                    consultant_address = address,
                    editor = editor)
        return consultant

    def __str__(self):
        return self.first_name + " " + self.last_name

'''
Represents a provider as an object containing all of their personal information.
Contains no information about relationship with clients or packages
'''
class Provider(models.Model):
    payment = models.IntegerField(default = 0, blank = True, null = True)
    first_name = models.CharField(max_length = 100, blank = True, null = True)
    last_name = models.CharField(max_length = 100, blank = True, null = True)
    provider_specialty = models.CharField(max_length = 50, choices=enums.SPECIALTIES, default = enums.SPECIALTIES[0][0], blank = True, null = True)
    provider_address = models.CharField(max_length = 200, blank = True, null = True)

    @staticmethod
    def FindProvidersByName(name):
        name_arr = name.split(" ") #split potential first and last name
        name_arr = [item for item in name_arr if item != ""] #remove empty strings
        if len(name_arr) == 0: #no name given, display everything
            return Provider.objects.order_by('first_name', 'last_name').all()
        elif len(name_arr) == 1: #just first name or last name
            by_first_name = Provider.objects.filter(first_name=name_arr[0]).order_by('first_name', 'last_name').all()
            by_last_name = Provider.objects.filter(last_name=name_arr[0]).order_by('first_name', 'last_name').all()
            if len(by_first_name) > len(by_last_name):
                return by_first_name
            return by_last_name
        else: #first and last name
            return Provider.objects.filter(first_name=name_arr[0], last_name=name_arr[1]).order_by('first_name', 'last_name').all()

    def CreateProvider(cls, payment, first_name, last_name, specialty, address):
        provider = cls(payment = payment,
                    first_name = first_name,
                    last_name = last_name,
                    provider_specialty = specialty,
                    provider_address = address)
        return provider

    def __str__(self):
        return self.first_name + " " + self.last_name

'''
Represents a client who may have a consultant and one or more packages
'''
class Client(models.Model):
    first_name = models.CharField(max_length = 100, blank = True, null = True)
    last_name = models.CharField(max_length = 100, blank = True, null = True)

    @staticmethod
    def FindClientsByName(name):
        name_arr = name.split(" ") #split potential first and last name
        name_arr = [item for item in name_arr if item != ""] #remove empty strings
        if len(name_arr) == 0: #no name given, display everything
            return Client.objects.order_by('first_name', 'last_name').all()
        elif len(name_arr) == 1: #just first name or last name
            by_first_name = Client.objects.filter(first_name=name_arr[0]).order_by('first_name', 'last_name').all()
            by_last_name = Client.objects.filter(last_name=name_arr[0]).order_by('first_name', 'last_name').all()
            if len(by_first_name) >= len(by_last_name):
                return by_first_name
            return by_last_name
        else: #first and last name
            return Client.objects.filter(first_name=name_arr[0], last_name=name_arr[1]).order_by('first_name', 'last_name').all()

    def CreateClient(cls, first_name, last_name):
        client = cls(first_name = first_name,
                    last_name = last_name)
        return client
    #returns client name as a string
    def __str__(self):
        return self.first_name + " " + self.last_name


'''
Representation of a list of services as a container for entries of that type
'''
class ServiceList(models.Model):
    client = models.ForeignKey(Client)

    @staticmethod
    def GetList(client):
        adlist = AddmissionsList.objects.select_related().get(client=client)
        return adlist

    def GetServices(self):
        return [entry.service for entry in self.serviceentry_set.all()]

    def GetProviders(self):
        return [entry.provider for entry in self.serviceentry_set.all()]

    def __str__(self):
        base_str = str(self.client) + " with services: "
        for service in self.GetServices():
            base_str += str(service) + ", "
        return base_str

'''
Entry of a non admissions related service
'''
class ServiceEntry(models.Model):
    container = models.ForeignKey(ServiceList, db_index = True)
    service = models.CharField(max_length = 20, choices = enums.POSSIBLE_SERVICES, default = enums.POSSIBLE_SERVICES[0][0], blank = True, null = True, db_index = True)
    start_date = models.DateField(default = datetime.now, blank = True, null = True, db_index = True)
    end_date = models.DateField(default = datetime.now, blank = True, null = True, db_index = True)
    provider = models.ForeignKey(Provider, db_index = True)

    def __str__(self):
        return str(self.service) + " by " + str(self.provider) + " for " + str(self.container.client)

'''
Representation of a list of addmissions as a container for entries of that type
'''
class AddmissionsList(models.Model):
    client = models.ForeignKey(Client)

    @staticmethod
    def GetList(client):
        adlist = AddmissionsList.objects.select_related().get(client=client)
        return adlist

    def GetAddmissionsServices(self):
        return [entry.service for entry in self.addmissionsentry_set.all()]

    def GetAddmissionsConsultants(self):
        return [entry.consultant for entry in self.addmissionsentry_set.all()]

    def __str__(self):
        return self.GetAddmissionsServices()

'''
Entry of an admissions related service
'''
class AddmissionsEntry(models.Model):
    container = models.ForeignKey(AddmissionsList, db_index = True)
    service = models.CharField(max_length = 20, choices = enums.POSSIBLE_ADMISSIONS_SERVICES, default = enums.POSSIBLE_ADMISSIONS_SERVICES[0][0], blank = True, null = True, db_index = True)
    start_date = models.DateField(default = datetime.now, blank = True, null = True, db_index = True)
    end_date = models.DateField(default = datetime.now, blank = True, null = True, db_index = True)
    consultant = models.ForeignKey(Consultant, db_index = True)

'''
Representation of a list of schools as a container which can hold school enums
'''
class SchoolList(models.Model):
    entry = models.ForeignKey(AddmissionsEntry, db_index = True)

    def GetSchools(self):
        return [entry.school for entry in self.schoolentry_set.all()]

    def __str__(self):
        return self.GetSchools()

'''
Entry in a list
'''
class SchoolEntry(models.Model):
    owning_list = models.ForeignKey(SchoolList, db_index = True)
    school = models.CharField(max_length = 100, choices = enums.SCHOOLS, default = enums.SCHOOLS[0][0], blank = True, null = True, db_index = True)
