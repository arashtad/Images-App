from django.db import models

class Posts(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
