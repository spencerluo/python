# coding=utf-8
import unittest

from ola import getResponse


class MyTestCase(unittest.TestCase):
    def test_sing(self):
        response = getResponse('听刘德华的忘情水')
        self.assertEqual(u'刘德华', response[0]['desc_obj']['artist'])
        self.assertEqual(u'music', response[0]['desc_obj']['type'])
        self.assertEqual(u'忘情水', response[0]['desc_obj']['title'])

    def test_singer(self):
        response = getResponse('周杰伦的歌')
        self.assertEqual(u'周杰伦', response[0]['desc_obj']['artist'])
        self.assertEqual(u'music', response[0]['desc_obj']['type'])
        self.assertEqual(u'', response[0]['desc_obj']['title'])

    def test_listen(self):
        response = getResponse('听歌')
        self.assertEqual(u'play_music', response[0]['type'])


if __name__ == '__main__':
    unittest.main()
