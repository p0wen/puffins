from django.db import models
from django.utils.text import slugify

from useraccount.models import UserAccount


class BlogPost(models.Model):
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=False, blank=True)
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    title_image = models.ImageField(null=True, blank=True)
    title_image_url_1 = models.URLField(max_length=1024, null=True, blank=True)
    content_image_1 = models.ImageField(null=True, blank=True)
    content_image_url_1 = models.URLField(max_length=1024, null=True, blank=True)
    content_image_2 = models.ImageField(null=True, blank=True)
    content_image_url_2 = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while BlogPost.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
