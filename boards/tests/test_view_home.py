
from django.test import TestCase
from django.urls import reverse, resolve
from boards.models import Board
from boards.views import home

# Create your tests here.
class HomeTests(TestCase):
    def setUp(self) -> None:
        self.board = Board.objects.create(name='好词', description='这是关于好词的素材版')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_status_code(self):
        self.assertEquals(self.response.status_code, 200)
    
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
    
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
