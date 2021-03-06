from django.shortcuts import render
from blog.models import blogger,blog,comment
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog.forms import CommentForm,BloggerForm,BlogForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import urllib2
import json




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

def register(request,uid):
	p = request.POST
	use =  request.user
	social = use.social_auth.get(provider='facebook')

	if p.has_key("username") and p["username"]:
		bid = uid
		blgr = blogger(bid=bid,name = str(social.user))
		blgr_frm = BloggerForm(p, instance = blgr)
		blgr_frm.save()
		print "yes saved"
	return HttpResponseRedirect(reverse("blog.views.welcome"))	


def addblog(request):
		p = request.POST
		use = request.user
		social = use.social_auth.get(provider= 'facebook')
		blog_by = blogger.objects.get(name = str(social.user))
		if p.has_key("title") and p["title"] and p.has_key("body") and p["body"]:
			blog_request = blog(blogger=blog_by,slug=slugify(p["title"]))
			blog_form = BlogForm(p, instance = blog_request)
			blog_form.save()
		return HttpResponseRedirect(reverse("blog.views.welcome"))

def welcome(request):
	if str(request.user) == "AnonymousUser":
		return HttpResponseRedirect(reverse("blog.views.home"))
	else:
		user =  request.user
		social = user.social_auth.get(provider='facebook')
		print social.uid
		print social.user
		if blogger.objects.filter(bid=social.uid).exists():
			ans = True
		else:
			ans = False
		
		posts = blog.objects.order_by("-posted_on").filter(blogger = (social.uid))
		context = RequestContext(request, {'uid':social.uid,'name':social.user,'form':BloggerForm(),'blogger':blogger,'ans':ans,'blog':posts})
		return render_to_response('welcome.html',context)
		
def create(request,uid):
	if str(request.user) == "AnonymousUser":
		return HttpResponseRedirect(reverse("blog.views.home"))
		print request.user
	else:
		name = blogger.objects.get(bid=uid)
		c= {'form':BlogForm(),'user':name}
		c.update(csrf(request))
	return render_to_response('create.html',c)

def index(request):
	return render_to_response('video_bg.html');



			

	