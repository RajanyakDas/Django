from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 1. Columns shown in the list
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    
    # 2. Sidebar filters
    list_filter = ['status', 'created', 'publish', 'author']
    
    # 3. Search bar functionality
    search_fields = ['title', 'body']
    
    # 4. Auto-generate slug from title
    prepopulated_fields = {'slug': ('title',)}
    
    # 5. Search widget for author (instead of dropdown)
    raw_id_fields = ['author']
    
    # 6. Navigation by date
    date_hierarchy = 'publish'
    
    # 7. Default sorting
    ordering = ['status', 'publish']

    show_facets = admin.ShowFacets.ALWAYS