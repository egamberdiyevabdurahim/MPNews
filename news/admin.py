from django.contrib import admin
from news.models import (CategoryModel, TagModel, AuthorModel, NewsModel, NewsCollectionModel, ContactModel,
                         NewsLetterModel)


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('name', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('first_name', 'last_name', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('name', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author__first_name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('title', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'subject')
    ordering = ('-created_at',)
    search_fields = ('full_name', 'message',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


admin.site.register(NewsCollectionModel)


@admin.register(NewsLetterModel)
class NewsLetterModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at')
    list_display_links = list_display
    ordering = ('-created_at',)
    search_fields = ('email', 'id')
