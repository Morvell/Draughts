import unittest
import Hahkiapi

class Test(unittest.TestCase):

  def test_how_kill(self):
      self.assertEqual(Hahkiapi.how_kill(), 'kletka')


