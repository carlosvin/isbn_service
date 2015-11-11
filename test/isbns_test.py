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


if __name__ == '__main__':
    unittest.main()