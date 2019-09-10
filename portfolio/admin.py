from django.contrib import admin
from .models import Project,Service

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
      
@admin.register(Service)      
class ServiceAdmin(admin.ModelAdmin):
      pass
#admin.site.register(Project,ProjectAdmin)
#admin.site.register(Service,ProjectAdmin)


