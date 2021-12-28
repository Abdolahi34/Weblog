from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    # Author

    def __str__(self):
        return self.title
    def body_preview(self):
        return self.body[:50] + ' ...'

