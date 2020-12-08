from django.shortcuts import render,HttpResponse
from .models import blog,blogcomments
from django.views.generic import DetailView,ListView
from django.core.paginator import Paginator
from .forms import newcommentform

# Create your views here.
#def home(request):
    #blg=blog.objects.all()
    #return render(request,'blog.html',{"blg":blg})

#def bpage(request):
    #blg=blog.objects.all()
    #return render(request,'blogpage.html',{"blg":blg})

class blogview(ListView):
    model = blog
    template_name="blog.html"
    paginate_by=2
    ordering=["-datetime"]

class postdetail(DetailView):
    model = blog
    template_name="blogpage.html"
    def get_context_data(self,**kwargs):
        data=super().get_context_data(**kwargs)
        comments_connected=blogcomments.objects.filter(blog=self.get_object()).order_by('-timestamp')
        data['comments']=comments_connected
        if self.request.user.is_authenticated:
            data['commentform']=newcommentform(instance=self.request.user)
        return data

    def post(self,request,*args,**kwargs):
        new_comment=blogcomments(comment=request.POST.get('comment'),user=self.request.user,blog=self.get_object())
        new_comment.save()
        return self.get(self,request,*args,**kwargs)


def search(request):
    query=request.GET['query']
    object_list=blog.objects.filter(content__icontains=query)
    params={'object_list':object_list}
    return render(request,'search.html',params)