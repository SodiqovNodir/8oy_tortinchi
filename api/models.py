from django.db import models


class Title(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

