from django.contrib import admin

from .models import member, event

# Register your models here.
admin.site.register(member)
admin.site.register(event)
