from django.contrib import admin

# Register your models here.
from app.models import *
class webpageAdminView(admin.ModelAdmin):
    list_display=['Topic_name','name','url']
    list_editable=['url']
    list_display_links=['name','Topic_name']
    list_per_page=2
    list_filter=['name','Topic_name']
    search_fields=['name']


admin.site.register(Topic)

admin.site.register(Webpage,webpageAdminView)

admin.site.register(Acessrecords)
