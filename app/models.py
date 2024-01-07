from django.db import models


class JobPost(models.Model):
    title = models.CharField(max_length=100)

