from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    '''
        Holds structure of the Portfolio relation in the DB
    '''
    project_title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=70)
    project_cover_pic = models.ImageField(upload_to='uploads/coverpics/', blank=True)
    client = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=50, blank=True)
    project_description = models.TextField(max_length=500, blank=True)
    project_link = models.URLField(blank=True)

    def __str__(self):
        return self.project_title

class Blog(models.Model):
    '''
        Holds structure of the Blog relation in the DB
    '''
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=70)
    author_profile_pic = models.ImageField(upload_to="uploads/authorprofilepics/", blank=True, null=True)
    author_profile = models.TextField(max_length=250)
    author_link_fb = models.URLField(blank=True)
    author_link_li = models.URLField(blank=True)
    author_link_tw = models.URLField(blank=True)
    author_link_ig = models.URLField(blank=True)
    article = models.TextField(max_length=None)
    publish_time = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.blog_title
