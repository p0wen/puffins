from .models import BlogPost
from django.contrib import admin


class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    readonly_fields = ('slug',)


admin.site.register(BlogPost, BlogPostAdmin)

