from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='home_page/images/')
    url = models.URLField(blank=True)             #MIGHT NOT NEED THIS!

    def __str__(self):                                                          #function sets name of each object on admin site
        return self.title
