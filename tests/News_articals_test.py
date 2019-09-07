import unittest
from app.models import News_article

class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_article = News_article("piclink","This article is about ...","3.06am","link to article")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article,News_article))