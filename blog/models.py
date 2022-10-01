import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Category(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    slug = models.SlugField('slug', unique=True)
    name = models.CharField('name', max_length=20)
    description = models.TextField('description', blank=True, null=True)
    display_order = models.IntegerField('display_order', default=0)

    class Meta:
        ordering = ('display_order', 'slug')
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    slug = models.SlugField('slug', unique=True)
    name = models.CharField('name', max_length=20)
    description = models.TextField('description', blank=True, null=True)

    class Meta:
        ordering = ('slug',)
        verbose_name_plural = 'Tags'

    def display(self):
        return '#' + self.name

    def __str__(self):
        return self.name


class PostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(
            is_published=True,
            published_at__lte=timezone.now(),
        )


class Post(models.Model):
    objects = PostQuerySet.as_manager()
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    slug = models.SlugField('slug', unique=True)
    title = models.CharField('title', max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='category'
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='tags')
    eye_catch = models.ImageField(
        'eye_catch', upload_to='blog/', blank=True, null=True
    )
    keywords = models.CharField('keywords', max_length=250)
    description = models.CharField('description', max_length=250)
    body = MarkdownxField('body')
    page_views = models.PositiveBigIntegerField('page_views', default=0)
    related_posts = models.ManyToManyField(
        'self', blank=True, verbose_name='related_posts'
    )
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    published_at = models.DateTimeField('published_at', default=timezone.now)
    updated_at = models.DateTimeField('updated_at', auto_now=True)
    is_published = models.BooleanField('is_published', default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        verbose_name='author'
    )

    def get_category_name(self):
        return self.category.name

    def get_tag_names(self):
        return [tag.display() for tag in self.tags.all()]

    def convert_md_to_html(self):
        return mark_safe(markdownify(self.body))

    def display_date(self, datetime):
        return datetime.strftime('%Y-%m-%d')

    def display_published_at(self):
        return self.display_date(self.published_at)

    def display_updated_at(self):
        return self.display_date(self.updated_at)

    class Meta:
        ordering = ('-updated_at',)
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
