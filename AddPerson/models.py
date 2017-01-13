from django.db import models
import AddPerson.enumerations as enums
# Create your models here.

'''
Represents an application.
'''
class Application(models.Model):
    application_round = models.IntegerField()
    application_school = models.CharField(max_length = 10, choices = enums.SCHOOLS)
    application_success = models.BooleanField(default=False)

    def __str__(self):
        return self.application_school

'''
Represents a consultant as an object containing all of their personal information.
Contains no information about relationship with clients or packages
'''
class Consultant(models.Model):
    consultant_first_name = models.CharField(max_length = 100)
    consultant_last_name = models.CharField(max_length = 100)
    consultant_specialty = models.CharField(max_length = 50, choices=enums.SPECIALTIES)
    consultant_address = models.CharField(max_length = 200)

    def __str__(self):
        return self.consultant_first_name + " " + self.consultant_last_name

'''
Represents a package as a package name and dates during which package is active/paid for
Contains no information about which clients have this package
'''
class Package(models.Model):
    package_name = models.CharField(max_length = 1, choices=enums.POSSIBLE_PACKAGES)
    package_start_date = models.DateField()
    package_end_date = models.DateField()

    #params: new_end_date, a datetime object representing the new end date of the package
    def ChangeEndDate(self, new_end_date):
        self.package_end_date = new_end_date

    #returns package name as a string
    def __str__(self):
        return self.package_name

'''
Represents a client who may have a consultant and one or more packages
'''
class Client(models.Model):
    client_first_name = models.CharField(max_length = 100)
    client_last_name = models.CharField(max_length = 100)
    client_packages = models.ManyToManyField(Package)
    client_consultant = models.ForeignKey(Consultant, on_delete = models.CASCADE)
    client_application = models.ManyToManyField(Application)
    #other info

    #params: new_package to add to the client
    def AddPackage(self, new_package):
        self.client_packages.add(new_package)

    #returns client name as a string
    def __str__(self):
        return self.client_first_name + " " + self.client_last_name
