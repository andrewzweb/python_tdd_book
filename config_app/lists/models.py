from django.db import models
from django.core.urlresolvers import reverse


class List(models.Model):
    '''list'''
    
    def get_absolute_url(self):
        '''get absolute url'''
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    '''item'''
    text = models.TextField(default='',blank=False, unique=True)
    list = models.ForeignKey(List,default=None)


    class Meta: 
        ordering = ('id',)
        unique_together = ('list', 'text')

        
    def __str__(self):
        return self.text
        
