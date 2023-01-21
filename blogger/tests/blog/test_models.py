import pytest

# access to db
pytestmark = pytest.mark.django_db


class TestPostModel:
    post_title = "test_post"

    def test_str_return(self, post_factory):
        post = post_factory(title=self.post_title)
        assert post.__str__() == self.post_title
