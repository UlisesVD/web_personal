from django.contrib import admin
from .models import Project

# Register your models here.
# extender funcionalidades del panel de control
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Project, ProjectAdmin)
