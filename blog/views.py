from django.shortcuts import render
from blog.models import blogger,blog
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index(request):
	return render_to_response('index.html',{
		'blog': blog.objects.all()
		})

def view_post(request,slug):
	return render_to_response('view_blog.html',{
		'blog': get_object_or_404(blog, slug=slug)
		})

def home(request):
	posts = blog.objects.all().order_by("-posted_on")
	paginator = Paginator(posts,5)

	try:
		page = int(request.GET.get("page","1"))
	except ValueError: page = 1

	try:
		posts = paginator.page(page)
	except(InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)


	context = RequestContext(request, {'request':request,'user':request.user,'blog': posts})
	return render_to_response('homeauth.html',context_instance=context)

# Create your views here.
