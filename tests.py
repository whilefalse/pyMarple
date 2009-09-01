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

    def test_invalid_postcode(self):
        self.assertRaises(pymarple.PostcodeNotFound, pymarple.find, 'not a postcode')

    def test_empty_postcode(self):
        self.assertRaises(pymarple.PostcodeNotFound, pymarple.find, '')

    def test_postcode_wrong_type(self):
        self.assertRaises(pymarple.PostcodeNotFound, pymarple.find, 100)

    def test_postcode_none(self):
        self.assertRaises(pymarple.PostcodeNotFound, pymarple.find, None)

    def test_url_unreachable(self):
        pymarple.url = "http://meh/"
        self.assertRaises(pymarple.PostcodeNotFound, pymarple.find, 'b27 6eg')

if __name__ == "__main__":
    unittest.main()