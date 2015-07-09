from django import forms
from blog.models import comment,blogger


class CommentForm(forms.ModelForm):
	class Meta:
		model = comment
		fields = ['author','body']


class BloggerForm(forms.ModelForm):
	class Meta:
		model = blogger
		fields = ['username']		