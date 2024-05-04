from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from .githubapi import search_repositories
from .models import Repository
from .githubapi import search_repositories

class RepositoryModelTest(TestCase):
    def test_string_representation(self):
        repo = Repository(name="Test Repo")
        self.assertEqual(str(repo), repo.name)

class SearchRepositoriesTest(TestCase):
    def test_api_search(self):

        response = search_repositories("django")
        self.assertIn('items', response)
        self.assertIsInstance(response['items'], list)

class ViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):

        response = self.client.get('/search/?q=django')
        self.assertEqual(response.status_code, 200)
