from django.contrib import admin
from blog.models import blog,blogger

class BlogAdmin(admin.ModelAdmin):
	fields = ['title','slug','body','blogger']
	prepopulated_fields = {'slug':('title',)}

admin.site.register(blogger)
admin.site.register(blog,BlogAdmin)

