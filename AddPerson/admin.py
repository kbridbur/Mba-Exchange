from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Package)
admin.site.register(Consultant)
admin.site.register(Application)

# Register your models here.
