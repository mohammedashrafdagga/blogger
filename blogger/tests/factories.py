import factory
from blogger.blog.models import Post
from django.contrib.auth.models import User


# create User Factory
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test"
    password = "test"
    is_superuser = True
    is_staff = True


# create post Factory
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "x"
    subtitle = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    slug = "x"
