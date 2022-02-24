from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'body')
    list_display = ('__str__', 'id', 'slug', 'created_at', 'updated_at')

admin.site.register(Post, PostAdmin)


