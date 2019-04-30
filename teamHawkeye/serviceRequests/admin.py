from django.contrib import admin
from .models import Request, Alert


admin.site.register(Request)
admin.site.register(Alert)
