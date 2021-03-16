from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
