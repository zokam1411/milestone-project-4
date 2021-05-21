from django.contrib import admin
from .models import News, Comment

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


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'news',
        'comment_author',
        'comment_text',
        'date_created',
    )


admin.site.register(Comment, CommentAdmin)
