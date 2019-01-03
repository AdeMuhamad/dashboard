from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, User


admin.site.site_header = 'Oapps Dashboard'

class PostAdmin(admin.ModelAdmin):
	list_display = ('user_id','title', 'subtitle', 'slug', 'content')
	list_filter = ('user_id','created_at')
	search_fields = ('content','title')

admin.site.register(Post, PostAdmin)

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','email','created_at')

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)
# Register your models here.
