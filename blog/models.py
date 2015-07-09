from django.db import models
from django.db.models import permalink

# Create your models here.

class blogger(models.Model):
	name = models.CharField(max_length = 200)
	username = models.CharField(max_length = 200, default ="username", unique = True)
	bid = models.IntegerField( primary_key=True,default = 0)
	def __str__(self):
		return self.name

class blog(models.Model):
	title = models.CharField(max_length = 200, unique = True)
	slug = models.SlugField(max_length = 200, unique = True)
	body = models.TextField()
	uid = models.AutoField(primary_key = True)
	posted_on = models.DateField(auto_now_add= True, db_index = True)
	blogger = models.ForeignKey(blogger)
	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return('view_blog_post', None, {'slug':self.slug})
	
class comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length = 60)
	body = models.TextField()
	post = models.ForeignKey(blog)
	def __str__(self):
		return self.body
