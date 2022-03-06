from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):                                                          #function sets name of each object on admin site
        return self.title
