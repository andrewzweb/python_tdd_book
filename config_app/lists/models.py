from django.db import models


class List(models.Model):
    '''list'''
    pass


class Item(models.Model):
    '''item'''
    text = models.TextField(blank=False)
    list = models.ForeignKey(List,default=None)

