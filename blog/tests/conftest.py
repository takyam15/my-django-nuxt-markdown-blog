import pytest

from blog.factories import CategoryFactory, TagFactory, PostFactory


@pytest.fixture
def category(db):
    return CategoryFactory()


@pytest.fixture
def tag(db):
    return TagFactory()


@pytest.fixture
def post(db):
    return PostFactory()
