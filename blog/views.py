from django.shortcuts import render
from blog.models import blogger,blog,comment
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.forms import CommentForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



def index(request):
	return render_to_response('index.html',{
		'blog': blog.objects.all()
		})

def view_post(request,slug):
	blog1 = blog.objects.get(slug = slug)
	cmnts = comment.objects.filter(post = blog1)
	context = {"blog":blog1,"comments":cmnts,"form":CommentForm(),"user":request.user}
	context.update(csrf(request))
	return render_to_response('view_blog.html',context)


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

def add_comment(request,id):
	
	p = request.POST 

	if p.has_key("body") and p["body"]:
		if p["author"]:
			author = p["author"]

		cmnt = comment(post = blog.objects.get(uid = id))
		cf = CommentForm(p, instance = cmnt)
		cf.fields["author"].required = False	

		comnt = cf.save(commit = False)
		comnt.author = author
		comnt.save()
		arg1=(blog.objects.get(uid = id)).slug 
	return HttpResponseRedirect(reverse("blog.views.view_post",args = [arg1]))
