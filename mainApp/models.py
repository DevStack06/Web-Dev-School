from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
import os
from uuid import uuid4
from mainApp.choices import *
from django.utils.deconstruct import deconstructible
import datetime

@deconstructible
class path_and_rename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

class Faculty(models.Model):
    namelen=150
    desclen=10000
    picfolder='faculty_pic/'
    category=models.IntegerField(choices=Faculty_choice, default=1)
    # defaultpic="no_image.png"
    name=models.CharField(max_length=namelen)
    pic=models.ImageField(upload_to=path_and_rename(picfolder))
    desc=models.CharField(max_length=desclen)
    email = models.EmailField(default=None, blank=True, null=True)
    qual=models.CharField(default=None, blank=True, null=True,max_length=namelen)
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def delete(self, *args, **kwargs):
        self.pic.delete()
        super(Picture, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(Faculty, self).save(*args, **kwargs)

    # def Faculty_pic_name(instance, filename):
    #     return '/'.join(['Faculty', instance.name, filename])

    def get_absolute_url(self):
        return reverse('addFaculty')





class Album(models.Model):
    namelen=150
    desclen=10000
    name=models.CharField(max_length=namelen)    
    desc=models.CharField(max_length=desclen)
    thumbnail=models.ImageField(null=True,blank=True)
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        super(Album, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('listAlbum')




class Photo(models.Model):
    picfolder='gallery_pic/'
    #defaultpic="no_image.png"
    name=models.CharField(max_length=150,null=True,blank=True)    
    albumid=models.ForeignKey("mainApp.Album", on_delete=models.CASCADE)
    pic=models.ImageField(upload_to=path_and_rename(picfolder))

    # def delete(self, *args, **kwargs):
        
    #     super(Photo, self).delete(*args, **kwargs)
    #     self.pic.delete()

    def get_absolute_url(self):
        return reverse('listPhoto',kwargs={'pk':self.albumid.id})
    
    def delete(self):
        self.pic.delete()
        super(Photo, self).delete()



def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class StudentAchiev(models.Model):
    
    namelen=100    
    picfolder='studentachiev/'
    name=models.CharField(max_length=namelen)
    institute=models.CharField(max_length=namelen)
    pic=models.ImageField(upload_to=path_and_rename(picfolder))
    category=models.IntegerField(choices=Cat_choice, default=1)
    year = models.IntegerField('year', choices=year_choices(), default=current_year)
    def get_absolute_url(self):
        return reverse('addStuAchive')
    
    def delete(self):
        self.pic.delete()
        super(Photo, self).delete()


class Review(models.Model):
    name=models.CharField(max_length=50)
    review=models.CharField(max_length=500)
    def get_absolute_url(self):
        return reverse('reviewlist')