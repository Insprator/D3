from django.db import models


class New(models.Model):
    title = models.CharField(max_length=64)
    Text = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return '{}' .format(self.title)
