from django.db import models
from datetime import datetime
import AddPerson.enumerations as enums

'''
Represents a consultants editor. conusltants may be their own editors in which case both objects will exist with the same name
Contains no information about who they edit
'''
class Editor(models.Model):
    payment = models.IntegerField(default = 0, blank = True, null = True)
    editor_first_name = models.CharField(max_length = 100, blank = True, null = True)
    editor_first_name = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return self.editor_first_name + " " + self.editor_last_name

'''
Represents a consultant as an object containing all of their personal information.
Contains no information about relationship with clients or packages
'''
class Consultant(models.Model):
    payment = models.IntegerField(default = 0, blank = True, null = True)
    consultant_first_name = models.CharField(max_length = 100, blank = True, null = True)
    consultant_last_name = models.CharField(max_length = 100, blank = True, null = True)
    consultant_specialty = models.CharField(max_length = 50, choices=enums.SPECIALTIES, default = enums.SPECIALTIES[0][0], blank = True, null = True)
    consultant_address = models.CharField(max_length = 200, blank = True, null = True)
    editor = models.ForeignKey(Editor)

    def CreateConsultant(cls, payment, first_name, last_name, specialty, address, editor):
        consultant = cls(payment = payment,
                    consultant_first_name = first_name,
                    consultant_last_name = last_name,
                    consultant_specialty = specialty,
                    consultant_address = address,
                    editor = editor)
        return consultant

    def __str__(self):
        return self.consultant_first_name + " " + self.consultant_last_name

'''
Represents a provider as an object containing all of their personal information.
Contains no information about relationship with clients or packages
'''
class Provider(models.Model):
    payment = models.IntegerField(default = 0, blank = True, null = True)
    provider_first_name = models.CharField(max_length = 100, blank = True, null = True)
    provider_last_name = models.CharField(max_length = 100, blank = True, null = True)
    provider_specialty = models.CharField(max_length = 50, choices=enums.SPECIALTIES, default = enums.SPECIALTIES[0][0], blank = True, null = True)
    provider_address = models.CharField(max_length = 200, blank = True, null = True)

    def CreateProvider(cls, payment, first_name, last_name, specialty, address):
        provider = cls(payment = payment,
                    provider_first_name = first_name,
                    provider_last_name = last_name,
                    provider_specialty = specialty,
                    provider_address = address)
        return provider

    def __str__(self):
        return self.provider_first_name + " " + self.provider_last_name

'''
Represents a client who may have a consultant and one or more packages
'''
class Client(models.Model):
    client_first_name = models.CharField(max_length = 100, blank = True, null = True)
    client_last_name = models.CharField(max_length = 100, blank = True, null = True)

    def CreateClient(cls, first_name, last_name):
        client = cls(client_first_name = first_name,
                    client_last_name = last_name)
        return client
    #returns client name as a string
    def __str__(self):
        return self.client_first_name + " " + self.client_last_name


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
