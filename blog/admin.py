from django.contrib import admin
from blog.models import blog,blogger,comment

class BlogAdmin(admin.ModelAdmin):
	fields = ['title','slug','body','blogger']
	prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
	fields = ['author','body','post']



admin.site.register(blogger)
admin.site.register(blog,BlogAdmin)
admin.site.register(comment,CommentAdmin)


