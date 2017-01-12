from django.db import models

# Create your models here.

'''
Represents a consultant as an object containing all of their personal information.
Contains no information about relationship with clients or packages
'''
class Consultant(models.Model):
    SPECIALTIES = (
        "specialty1",
        "specialty2",
        "specialty3"
    )
    consultant_first_name = models.CharField(max_length = 100)
    consultant_last_name = models.CharField(max_length = 100)
    consultant_specialty = models.CharField(max_length = 50, choices = SPECIALTIES)
    consultant_address = models.CharField(max_length = 200)

'''
Represents a package as a package name and dates during which package is active/paid for
Contains no information about which clients have this package
'''
class Package(models.Model):
    POSSIBLE_PACKAGES = (
        "package1",
        "package2",
        "package3"
    )
    package_name = models.CharField(max_length = 20, choices=POSSIBLE_PACKAGES)
    package_start_date = models.DateField()
    package_end_date = models.DateField()

    #params: new_end_date, a datetime object representing the new end date of the package
    def ChangeEndDate(self, new_end_date):
        package_end_date = new_end_date

    #returns package name as a string
    def __str__(self):
        return package_name

'''
Represents a client who may have a consultant and one or more packages
'''
class Client(models.Model):
    client_first_name = models.CharField(max_length = 100)
    client_last_name = models.CharField(max_length = 100)
    client_packages = models.ManyToManyField(Package)
    client_consultant = models.ForeignKey(Consultant, on_delete = CASCADE)
    #other info

    #params: new_package to add to the client
    def AddPackage(self, new_package):
        client_packages.add(new_package)

    #returns client name as a string
    def __str__(self):
        return client_first_name + " " + client_last_name
