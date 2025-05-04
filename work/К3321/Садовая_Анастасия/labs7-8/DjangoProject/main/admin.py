from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class ContactAdmin(admin.ModelAdmin):
    pass
