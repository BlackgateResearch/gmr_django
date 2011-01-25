from django.db import models

class Artist(models.Model):
    user =        models.ForeignKey('auth.User')
    name =        models.CharField(max_length = 50)
    description = models.TextField()
    picture =     models.ImageField(upload_to="artist/pictures")

    def __unicode__(self):
        return unicode(self.name)