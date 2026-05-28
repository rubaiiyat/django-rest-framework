from django.contrib import admin

from blogs.models import BlogsModel, CommentsModel
# Register your models here.
admin.site.register(BlogsModel)
admin.site.register(CommentsModel)