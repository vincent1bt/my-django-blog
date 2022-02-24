from django.db import models

# Create your models here.
import uuid

from django.utils import timezone

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Post(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False, unique=True)
    image = models.CharField(max_length=150, null=False, blank=False, unique=False)

    description = models.TextField(null=False, blank=False, unique=False)
    body = models.TextField(null=False, blank=False, unique=False)
    
    slug = models.SlugField(max_length=150, null=False, blank=False, unique=True)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Post.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8] )
            )

        instance.slug = slug

    instance.updated_at = timezone.now()

pre_save.connect(set_slug, sender=Post)