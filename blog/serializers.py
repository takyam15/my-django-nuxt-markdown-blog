from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Post


class PostSerializer(ModelSerializer):
    category = SerializerMethodField()
    tags = SerializerMethodField()
    body = SerializerMethodField()
    published_at = SerializerMethodField()
    updated_at = SerializerMethodField()

    def get_category(self, obj):
        return obj.get_category_name()

    def get_tags(self, obj):
        return obj.get_tag_names()

    def get_body(self, obj):
        return obj.convert_md_to_html()

    def get_published_at(self, obj):
        return obj.display_published_at()

    def get_updated_at(self, obj):
        return obj.display_updated_at()

    class Meta:
        model = Post
        exclude = ('id', 'is_published')
