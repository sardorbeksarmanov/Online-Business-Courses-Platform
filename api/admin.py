from django.contrib import admin
from .models import Serves, Clients, Advise, FAQs, Features, Comment
from import_export.admin import ImportExportModelAdmin

@admin.register(Serves)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'title', 'image')
    list_display_links = ('id', 'slug', 'title', 'image')
    search_fields = ('id', 'title')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Advise)
class AdvisersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'first_name', 'last_name', 'level', 'email')
    list_display_links = ('id', 'slug', 'first_name', 'last_name', 'level', 'email')
    search_fields = ('id', 'first_name')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('first_name',)}

@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number')
    search_fields = ('id', 'first_name')
    ordering = ('id',)

@admin.register(FAQs)
class FAQsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'questions', 'answers')
    list_display_links = ('id', 'questions', 'answers')
    ordering = ('id',)

@admin.register(Features)
class FeaturesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    ordering = ('id',)

@admin.register(Comment)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'comment')
    list_display_links = ('id', 'comment')
    ordering = ('id',)
