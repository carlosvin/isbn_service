import random
import unittest

from rest.isbns import isbn_parse, is_valid


class TestIsbn(unittest.TestCase):

    def test_isbn_parse(self):
        self.assertEqual(1234561234567, isbn_parse("123456-1234567"))
        self.assertEqual(1234561234567, isbn_parse("123,;456-1234567"))
        self.assertEqual(1000000000, isbn_parse("-10-00000000-"))
        self.assertEqual(1000000000, isbn_parse("asdf 10 sd00000000df d"))

    def test_is_valid(self):
        self.assertTrue(is_valid(1234567891))
        self.assertTrue(is_valid(1000000000))
        self.assertFalse(is_valid(999999999))
        self.assertFalse(is_valid(0))
        self.assertFalse(is_valid(1.0000000000))

    def test_is_valid_rnd(self):
        invalids = (random.randint(0, 999999999), random.randint(10000000000, 999999999999), random.randint(10000000000000, 9999999999999999))
        for x in invalids:
            self.assertFalse(is_valid(x), x)


if __name__ == '__main__':
    unittest.main()