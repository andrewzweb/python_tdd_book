from django.db import models


class List(models.Model):
    '''list'''
    pass


class Item(models.Model):
    '''item'''
    text = models.TextField(default='',blank=True,null=True)
    list = models.ForeignKey(List,default='')

