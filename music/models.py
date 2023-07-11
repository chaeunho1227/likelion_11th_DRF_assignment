from django.db import models

# Create your models here.
def image_upload_path(instance,filename):
    return f'{instance.pk}/{filename}'

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=30)

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=image_upload_path,blank=True,null=True)
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField(null=True,blank=True)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, blank=True)

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album,blank=False,null=False, on_delete=models.CASCADE,related_name='tracks')
    track_num = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
