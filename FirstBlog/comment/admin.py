from django.contrib import admin

from .models import Comment
from FirstBlog.custom_site import custom_site
from FirstBlog.base_admin import BaseOwnerAdmin


@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
