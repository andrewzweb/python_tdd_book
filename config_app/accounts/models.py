from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class Token(models.Model):
    '''tokens'''

    email = models.EmailField()
    uid = models.CharField(max_length=255)

class ListUserManager(BaseUserManager):
    '''manager of list'''

    def create_use(self, email):
        '''create user'''
        ListUser.objects.create(email=email)
        
    def create_superuser(self, email, password):
        '''create superuser'''
        self.createuser(email)


class ListUser(AbstractBaseUser, PermissionsMixin):
    '''user of list '''

    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['email', 'height']

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'mail@gmail.com'

    @property 
    def is_active(self):
        return True


