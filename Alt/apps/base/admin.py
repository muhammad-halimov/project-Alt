from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = models.User.DisplayFields
    search_fields = models.User.SearchableFields
    list_filter = models.User.FilterFields


@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = models.Tasks.DisplayFields
    search_fields = models.Tasks.SearchableFields
    list_filter = models.Tasks.FilterFields


@admin.register(models.Competition)
class CompetitionsAdmin(admin.ModelAdmin):
    list_display = models.Competition.DisplayFields
    search_fields = models.Competition.SearchableFields
    list_filter = models.Competition.FilterFields


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = models.Organization.DisplayFields
    search_fields = models.Organization.SearchableFields
    list_filter = models.Organization.FilterFields


@admin.register(models.History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = models.History.DisplayFields
    search_fields = models.History.SearchableFields
    list_filter = models.History.FilterFields
