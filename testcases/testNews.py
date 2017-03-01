# coding=utf-8
import unittest
from ola import getResponse


class MyTestCase(unittest.TestCase):
    def test_news(self):
        response = getResponse('新闻')
        self.assertEqual(u'news', response[0]['desc_obj']['type'])
        self.assertEqual(u'selection', response[0]['type'])
        self.assertEqual(9, len(response[0]['data_obj']))

if __name__ == '__main__':
    unittest.main()
