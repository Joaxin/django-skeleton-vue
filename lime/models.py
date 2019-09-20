from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager

User = settings.AUTH_USER_MODEL

class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(is_public='true')


class Category(models.Model):

    name = models.CharField(verbose_name='分类', max_length=20)
    description = models.TextField('description', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class PublicBookmarkManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicBookmarkManager, self).get_queryset()
        return qs.filter(is_public=True)


class Bookmark(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    url = models.URLField()
    ico = models.ImageField(upload_to='user/%Y/', blank=True)
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    is_valid= models.BooleanField('valid', default=True)

    created = models.DateTimeField('date created',auto_now_add=True)
    updated = models.DateTimeField('date updated',auto_now=True)
    pub_date = models.DateField('date published', default=timezone.now)

    category = models.ForeignKey(Category, verbose_name='网站分类',on_delete=models.CASCADE)
    tags=TaggableManager()

    objects = models.Manager()
    public = PublicManager()

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['title']

    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
