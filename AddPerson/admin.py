from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Consultant)
admin.site.register(Service)
admin.site.register(Provider)
admin.site.register(Editor)

# Register your models here.
