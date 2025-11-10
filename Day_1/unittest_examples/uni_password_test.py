import unittest

import Day_1.Practice.strong_password as strong_password


class TestPassword(unittest.TestCase):
    def test_check_password(self):
        self.assertTrue(all(strong_password.check_password("123456")))

    def test_check_password_one(self):
        self.assertTrue(all(strong_password.check_password("123456478!")))

    def test_check_password_two(self):
        self.assertTrue(all(strong_password.check_password("saucacAusacu8")))

    def test_check_password_three(self):
        self.assertTrue(all(strong_password.check_password("o58anuahaunH!")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
