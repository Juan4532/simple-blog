from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PostObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset() .filter(status='published')

class Post(models.Model):
    postobjects = PostObjects()

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),    
        )


    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique_for_date='published', null=False, unique=False)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title



class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f"Comentado por {self.name}"