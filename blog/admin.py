from django.contrib import admin
from blog.models import Post,blogComment
# Register your models here.
admin.site.register((Post,blogComment))