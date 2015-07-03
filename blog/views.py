from django.shortcuts import render
from blog.models import blogger,blog
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
	return render_to_response('index.html',{
		'blog': blog.objects.all()
		})

def view_post(request,slug):
	return render_to_response('view_blog.html',{
		'blog': get_object_or_404(blog, slug=slug)
		})

# Create your views here.
