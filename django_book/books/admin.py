from django.contrib import admin
from books.models import Publisher,Author,Book
# Register your models here.
class Authoradmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")
    search_fields = ('first_name','last_name')

class Bookadmin(admin.ModelAdmin):
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('title',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('authors',)

admin.site.register(Publisher)
admin.site.register(Author,Authoradmin)
admin.site.register(Book,Bookadmin)

