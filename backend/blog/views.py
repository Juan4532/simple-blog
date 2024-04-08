from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Post
from django.utils.safestring import mark_safe

# Create your views here.

class BlogHomePageView(TemplateView):
    template_name = "blog/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.all()
        return context



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.postobjects.filter(slug=self.kwargs.get('slug'))

        # Marcamos el contenido como seguro
        #post.content = mark_safe(post.content)
        context['post'].content = mark_safe(context['post'].content)
        return context