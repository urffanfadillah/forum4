from django.contrib import admin
# import models post
from .models import PostModel, CommentModel
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display    = [
        'author','title','image','category','created_at','slug'
    ]
    list_per_page   = 25
    search_fields   = [
        'author','title'
    ]
    list_filter     = [
        'category', 'created_at'
    ]

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()
# register PostModelAdmin
admin.site.register(PostModel, PostModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    list_display    = [
        'author', 'desc', 'post', 'created_at', 'active'
    ]
    list_filter     = [
        'active', 'created_at'
    ]
    search_fields   = [
        'author', 'desc'
    ]
    actions         = ['approve_comments']

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author  = request.user
        obj.save()
# register CommentModelAdmin
admin.site.register(CommentModel, CommentModelAdmin)
