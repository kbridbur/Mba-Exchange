from django.db import models

# Create your models here.


class Package(models.Model):
    POSSIBLE_PACKAGES = (
        "package1",
        "package2",
        "package3"
    )
    package_name = models.CharField(max_length = 20, choices=POSSIBLE_PACKAGES)
    package_start_date = models.DateField()
    package_end_date = models.DateField()

    def ChangeEndDate(self, new_end_date):
        package_end_date = new_end_date

    def __str__(self):
        return package_name

class Client(models.Model):
    client_first_name = models.CharField(max_length = 100)
    client_last_name = models.CharField(max_length = 100)
    package = models.ManyToManyField(Package)
    #other info

    def ChangePackage(self, new_package):
        self.package = new_package

    def __str__(self):
        return client_first_name + " " + client_last_name
