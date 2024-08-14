from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Blog

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@gmail.com',
            password = 'mysecretpassword'
        )

        self.blog = Blog.objects.create(
            title = 'A new blog',
            body = 'lorem ipsum et al',
            author = self.user
        )

    def test_string_representation(self):
        blog = Blog(title='A test title')
        self.assertEqual(str(blog), blog.title)

    def test_blog_content(self):
        self.assertEqual(self.blog.title, 'A new blog')
        self.assertEqual(self.blog.body, 'lorem ipsum et al')
        self.assertEqual(self.blog.author.username, 'testuser')

    def test_blog_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        # print(response.content.decode())
        self.assertContains(response, 'lorem ipsum et al')

    def test_blog_detail_view(self):
        response = self.client.get('/blog/1/')
        bad_response = self.client.get('/blog/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bad_response.status_code, 404)
        self.assertContains(response, 'lorem ipsum et al')
        self.assertTemplateUsed(response, 'blog_detail.html')
