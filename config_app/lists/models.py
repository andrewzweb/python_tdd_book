from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class List(models.Model):
    '''list'''

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    
    def get_absolute_url(self):
        '''get absolute url'''
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    '''item'''
    text = models.TextField(default='',blank=False, unique=True)
    list = models.ForeignKey(List,default=None)

    @property
    def name(self):
        '''name'''
        return self.item_set.first().text

    class Meta: 
        ordering = ('id',)
        unique_together = ('list', 'text')

        
    def __str__(self):
        return self.text
        
