from django.db import models


class Article(models.Model):
    Title = models.CharField(max_length=50)
    Body = models.TextField()
    Slug = models.SlugField()
    DateCreated = models.DateTimeField(auto_now_add=True)
    # Author
    # Image

    def __str__(self):
        return self.Title
    def BodyLittle(self):
        return self.Body[:50] + ' ...'

