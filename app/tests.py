import unittest

class MyTestClass(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
      pass

  @classmethod
  def tearDownClass(cls):
      pass

  def setUp(self):
      pass

  def tearDown(self):
      pass

  def test_dummy_one(self):
      self.assertEqual(3, 3)

  def test_dummy_two(self):
      self.assertEqual(True, True)