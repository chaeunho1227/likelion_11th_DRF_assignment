from django.db import models

# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField(null=True,blank=True)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album,blank=False,null=False, on_delete=models.CASCADE,related_name='tracks')
    track_num = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

