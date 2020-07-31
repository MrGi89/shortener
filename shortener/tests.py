from django.test import Client, TestCase
from django.urls import reverse


class UrlBaseViewTestCase(TestCase):

    def test_get_default_behavior(self):

        response = self.client.get(reverse('base_view'))
        self.assertEqual(response.status_code, 200)

    def test_post_default_behavior(self):

        response = self.client.post(reverse('base_view'), data={'url': 'www.example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('new_url', response.context)

    def test_post_bad_url(self):

        response = self.client.post(reverse('base_view'), data={'url': 'www.example.com/xxxx/xxxx/xxxx'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('form_errors', response.context)
        self.assertIn('url', response.context['form_errors'])
        self.assertIn('Bad url - connection error', response.context['form_errors']['url'])

    def test_post_unique_url(self):

        r1 = self.client.post(reverse('base_view'), data={'url': 'www.example.com'})
        r2 = self.client.post(reverse('base_view'), data={'url': 'www.example.com'})
        self.assertEqual(r1.status_code, 200)
        self.assertEqual(r2.status_code, 200)
        self.assertIn('new_url', r1.context)
        self.assertIn('new_url', r2.context)
        self.assertEqual(r1.context['new_url'], r2.context['new_url'])

    def test_post_wrong_parameter(self):

        response = self.client.post(reverse('base_view'), data={'urls': 'www.example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('url', response.context['form_errors'])
        self.assertIn('This field is required.', response.context['form_errors']['url'])


class UrlRedirectViewTestCase(TestCase):

    def test_get_default_behavior(self):

        r1 = self.client.post(reverse('base_view'), data={'url': 'www.example.com'})
        r2 = self.client.get(reverse('redirect_view', kwargs={'slug': r1.context['new_url'].slug}))

        self.assertRedirects(r2, 'http://www.example.com', fetch_redirect_response=False)


