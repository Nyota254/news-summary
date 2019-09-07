import unittest
from app.models import News_source

class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_source = News_source("cnn","world wide news provision","politics sports etc","https://www.newssource.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source,News_source))