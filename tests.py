import unittest
import pymarple

class TestErnestMarple(unittest.TestCase):
    def setUp(self):
        pass

    def test_birmingham(self):
        lat, long = pymarple.find('b27 6eg')
        self.assertAlmostEqual(lat, 52.450211,4)
        self.assertAlmostEqual(long, -1.816588,4)

    def test_london(self):
        lat, long = pymarple.find('e3 2bg')
        self.assertAlmostEqual(lat, 51.526966,4)
        self.assertAlmostEqual(long, -0.029495,4)

    def test_invalid(self):
        self.assertRaises(Exception, pymarple.find, 'not a postcode')


if __name__ == "__main__":
    unittest.main()