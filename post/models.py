from django.db import models
# import slugify
from django.utils.text import slugify
# import User
from django.contrib.auth.models import User
# import FroalaField
from froala_editor.fields import FroalaField

# Create your models here.
class PostModel(models.Model):
    CATEGORY_CHOICES        = (
        ('RPL','Rekayasa Perangkat Lunak'),
        ('TKJ','Teknik Komputer Jaringan'),
        ('TBSM','Teknik Bisnis Sepeda Motor'),
        ('umum','Umum'),
    )
    author      = models.ForeignKey(User, on_delete=models.CASCADE,editable=False, null=True, blank=True)
    title       = models.CharField(max_length=100)
    category    = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True)
    desc        = FroalaField()
    image       = models.ImageField(upload_to='thumbnail_image/' ,blank=True, default='thumbnail_image/forum-24px.svg')
    created_at  = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    slug        = models.SlugField(blank=True, editable=False) 

    def save(self):
        self.slug   = slugify(self.title)
        super(PostModel, self).save()

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    post        = models.ForeignKey(PostModel, on_delete=models.CASCADE,null=True, related_name='comments')
    author      = models.ForeignKey(User, on_delete=models.CASCADE,editable=False, null=True, blank=True)
    desc        = FroalaField()
    created_at  = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    active      = models.BooleanField(default=True)

    class Meta:
        ordering    = ['created_at']
    
    def __str__(self):
        return 'CommentModel {} by {}'.format(self.desc, self.author)