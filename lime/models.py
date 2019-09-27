from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager

User = settings.AUTH_USER_MODEL

class Category(models.Model):

    name = models.CharField(verbose_name='category', max_length=20)
    description = models.TextField('description', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')

    created = models.DateTimeField('date created',auto_now_add=True)
    updated = models.DateTimeField('date updated',auto_now=True)

    category = models.ForeignKey(Category, related_name='mensaje',on_delete=models.CASCADE)
    tags=TaggableManager()

    content = models.TextField(max_length=2000)
    
    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ['id']

    def __str__(self):
        return '%s (%s) (%s)' % (self.content, self.category, self.content)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
