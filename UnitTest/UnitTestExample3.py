import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("setup method which will exevute before every  test")

    def tearDown(self):
        print("teardown will execute after every test")

    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")


