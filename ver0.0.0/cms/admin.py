from django.contrib import admin
from .models import Post, Category, Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'title': ('slug',)}

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('slug', 'title', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'slug', 'user', 'n_e_p_v_i_s', 's_s_a')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
"""
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)
"""
