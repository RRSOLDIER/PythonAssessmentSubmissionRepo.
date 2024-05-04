from django.contrib import admin
from .models import Repository

#@admin.register(Repository)
admin.site.register(Repository)
#class RepositoryAdmin(admin.ModelAdmin):
    #list_display = ['name', 'owner', 'stars', 'forks']
