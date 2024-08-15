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

    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), '/blog/1/')

    def test_blog_create_view(self):
        response = self.client.post(reverse('new-blog'), {
            'title': 'New title',
            'body': 'New body',
            'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New body')

    def test_blog_update_view(self):
        response = self.client.post(reverse('edit-blog', args='1'), {
            'title': 'Updated title',
            'body': 'Updated body'
        })
        self.assertEqual(response.status_code, 302)

    def test_blog_delete_view(self):
        response = self.client.get(reverse('delete-blog', args='1'))
        self.assertEqual(response.status_code, 200)