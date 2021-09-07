from django.contrib import admin
from .models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')
    list_display = ('title', 'author', 'published', 'post_categories')

    def post_categories(self, obj):
        return f', '.join([c.name for c in obj.categories.all()])

    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
