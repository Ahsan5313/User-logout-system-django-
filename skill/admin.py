from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Myskill, ContactInfo

admin.site.register(Myskill)

admin.site.register(ContactInfo)