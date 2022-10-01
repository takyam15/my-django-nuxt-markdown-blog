from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Tag, Post
from .serializers import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):

    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.published()
        category_slug = self.request.query_params.get('category')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.select_related('category').filter(category=category)
        tag_slug = self.request.query_params.get('tag')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.prefetch_related('tags').filter(tags=tag)
        return queryset
