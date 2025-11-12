import unittest

import Day_2.Practice.encode_decode as ed


class TestEncodeDecode(unittest.TestCase):
    """Test encode"""

    def test_encode(self):
        self.assertEqual(ed.encode("070411111426152419071413"), "hello python")

    """Test dencode"""

    def test_dencoder(self):
        self.assertEqual(
            ed.decoder("hello python"), "070411111426152419071413"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
