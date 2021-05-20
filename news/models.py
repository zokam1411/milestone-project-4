from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class News(models.Model):

    class Meta:
        verbose_name_plural = 'News'

    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               )
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250,
                             unique=True,
                             null=False,
                             blank=False,
                             )
    introduction = models.TextField(null=False, blank=False,)
    content = models.TextField(null=False, blank=False,)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
