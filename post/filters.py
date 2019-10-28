# import models post
from .models import PostModel
# import django_filters
import django_filters

class PostFilter(django_filters.FilterSet):
    class Meta:
        model       = PostModel
        fields      = [
            'author','title','category'
        ]