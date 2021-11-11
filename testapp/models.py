from django.db import models

# Create your models here.

class NewModel(models.Model):
	amount = models.CharField(max_length=255), 
	start_date = models.DateField()
	expiry_date = models.DateField(),    

    # def __str__(self):
    #     return self.amount


class TestModel(models.Model):
    key1 = models.CharField(max_length=200)
    coverage_requirements = models.ForeignKey(NewModel, on_delete=models.CASCADE)
    key2 = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.key1



class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)