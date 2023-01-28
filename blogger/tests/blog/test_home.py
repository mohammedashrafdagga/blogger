import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


# Tow Test (first check the main page run correctly)
class TestHomePage:
    # pass
    def test_home_page_url(self, client):
        url = reverse("blog:homepage")
        response = client.get(url)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client):
        headers = {"HTTP_HX-Request": "true"}
        url = reverse("blog:homepage")
        response = client.get(url, **headers)
        assertTemplateUsed(response, "blog/components/post-list-elements.html")
