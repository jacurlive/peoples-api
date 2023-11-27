from django.contrib import admin
from .models import Peoples, Category
# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'nickname', 'is_published', 'birth_date', 'cat')
    list_editable = ('is_published',)
    list_display_links = ('name', 'last_name')
    search_fields = ('name', 'last_name', 'nickname')
    list_filter = ('cat',)


admin.site.register(Peoples, PeopleAdmin)
admin.site.register(Category)
