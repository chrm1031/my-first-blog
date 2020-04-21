from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# PostモデルをAdminページ（管理画面）上で見えるようにするため、
# admin.site.register(Post)でモデルを登録する必要がある
admin.site.register(Post)
admin.site.register(Comment)
