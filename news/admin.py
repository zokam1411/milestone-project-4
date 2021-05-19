from django.contrib import admin
from .models import News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'author',
        'date_created',
    )

    search_fields = [
        'title',
        'content',
    ]

admin.site.register(News, NewsAdmin)
