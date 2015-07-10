from django import forms
from blog.models import comment,blogger,blog


class CommentForm(forms.ModelForm):
	class Meta:
		model = comment
		fields = ['author','body']


class BloggerForm(forms.ModelForm):
	class Meta:
		model = blogger
		fields = ['username']		

class BlogForm(forms.ModelForm):
	class Meta:
		model = blog
		fields = ['title','body']