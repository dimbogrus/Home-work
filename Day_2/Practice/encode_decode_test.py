import unittest

import encode_decode as ed


class TestEncodeDecode(unittest.TestCase):
    """Test encode"""
    def test_encode(self):
        self.assertEqual(ed.encode('070411111426152419071413'), 'hello python')
        self.assertRaises(TypeError, ed.encode, 110411111426152419071413)
        self.assertRaises(ValueError, ed.encode, 'hello python')

    """Test dencode"""
    def test_dencoder(self):
        self.assertEqual(ed.decoder('hello python'), '070411111426152419071413')
        self.assertRaises(TypeError, ed.decoder, 110411111426152419071413)

if __name__ == "__main__":
    unittest.main(verbosity=2)