import unittest
import pymarple

class TestErnestMarple(unittest.TestCase):
    def setUp(self):
        pass

    def test_birmingham(self):
        lat, long = pymarple.find('b27 6eg')
        self.assertEqual(lat, 52.450211)
        self.assertEqual(long, -1.816588)

    def test_london(self):
        lat, long = pymarple.find('e3 2bg')
        self.assertEqual(lat, 51.526966)
        self.assertEqual(long, -0.029495)

    def test_invalid(self):
        lat, long = pymarple.find('not a postcode fool')
        self.assertRaises(Exception)


if __name__ == "__main__":
    unittest.main()