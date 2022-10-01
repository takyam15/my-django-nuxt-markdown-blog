from factory import SubFactory
from factory.django import DjangoModelFactory

from .models import Category, Tag, Post
from account.factories import UserFactory


class CategoryFactory(DjangoModelFactory):
    name = 'Test Category'
    slug = 'test-category'

    class Meta:
        model = Category
        django_get_or_create = ('name', 'slug')


class TagFactory(DjangoModelFactory):
    name = 'Test Tag'
    slug = 'test-tag'

    class Meta:
        model = Tag
        django_get_or_create = ('name', 'slug')


class PostFactory(DjangoModelFactory):
    title = 'Test Post'
    slug = 'test-post'
    category = SubFactory(CategoryFactory)
    tags = [SubFactory(TagFactory)]
    keywords = 'tests'
    description = 'This is a test post.'
    body = '## Subtitle\ntext'
    is_published = True
    author = SubFactory(UserFactory)

    class Meta:
        model = Post
        django_get_or_create = ('title', 'slug')
